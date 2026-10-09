'''信息弹窗：界面在 info_window.py（pyuic 生成的），逻辑放这里

用法：
    idx = InfoDialog.ask(self, "未保存的更改", "要怎么处理？", ["取消", "丢弃", "保存"])
    # 返回被点击按钮在列表里的下标（从 0 开始）；直接关掉窗口或者按 Esc 返回 -1

按钮摆放（按你的预设）：
    三个 → 左 / 中 / 右
    两个 → 左 / 右（中间的藏起来）
    一个 → 只占右边（左边和中间的都藏起来）
'''

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from info_window import Ui_Dialog
from ui_common import load_qss


class InfoDialog(QDialog):
    '''统一的提示/确认弹窗'''

    def __init__(self, owner=None, title="", message="", buttons=("确定",), danger=None):
        super().__init__(owner)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)   # 和主窗口一样不要系统边框
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet(load_qss())                            # 和主窗口共用一份样式
        self.setWindowModality(Qt.ApplicationModal)               # 开着的时候别去点主窗口
        self.result_index = -1                                    # 没点按钮就关掉的话留这个

        self.ui.title.setText(title)
        self.ui.message.setText(message)

        # 按「右边的按钮最重要」来摆，最后一个放在右边
        slots = [self.ui.btnLeft, self.ui.btnMiddle, self.ui.btnRight]
        buttons = list(buttons)[:3]
        if len(buttons) == 1:
            used = [self.ui.btnRight]
        elif len(buttons) == 2:
            used = [self.ui.btnLeft, self.ui.btnRight]
        else:
            used = slots

        # 没用的按钮藏起来
        for slot in slots:
            slot.setVisible(slot in used)

        self._used = used
        for i, text in enumerate(buttons):
            used[i].setText(text)
            used[i].clicked.connect(lambda _=False, index=i: self._finish(index))
            # 危险操作（丢弃、确认放弃之类）挂个标记，样式交给 QSS 的 [danger="true"]
            used[i].setProperty("danger", "true" if i == danger else "false")
            used[i].style().unpolish(used[i])
            used[i].style().polish(used[i])

        self.adjustSize()

    def _finish(self, index):
        '''记下点了哪个按钮，然后关窗'''

        self.result_index = index
        self.accept()

    @staticmethod
    def ask(owner, title, message, buttons, danger=None):
        '''开一个弹窗，把被点的按钮下标返回给调用方

        danger：哪个下标是「危险操作」（会变成淡红色），不传就没有
        '''

        dialog = InfoDialog(owner, title, message, buttons, danger)
        dialog.exec()
        return dialog.result_index


if __name__ == "__main__":      # 单独跑可以直接看效果
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    for btns in (["确定"], ["取消", "确认"], ["取消", "丢弃", "保存"]):
        print(btns, "->", InfoDialog.ask(None, "标题示例", "这里是一段提示文字。", btns))
