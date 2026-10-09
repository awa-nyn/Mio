'''第二页：修改设定

界面在 GUI.py（pyuic 生成的）里，这里只放逻辑。
- 进页面时从 core/system_.py 读数据填进文本框，空的就把 description 当灰色占位文字
- 每次文本框有变动就重新比对一次，改回原样又会变回「没改过」
- 保存 / 取消 / 关闭 三种收尾，最后都回第一页
'''

import json
import sys
from pathlib import Path

# 让 GUI 里的代码能 import 到 Agent/core（GUI 目录的上一层）
AGENT_DIR = Path(__file__).parent.parent
if str(AGENT_DIR) not in sys.path:
    sys.path.append(str(AGENT_DIR))

from core.system_ import prmpt     # noqa: E402

from PySide6.QtWidgets import QLineEdit     # noqa: E402

from info_dialog import InfoDialog  # noqa: E402


def _text_of(box):
    '''取框里的内容：单行框和多行框的接口不一样'''

    return box.text() if isinstance(box, QLineEdit) else box.toPlainText()


def _set_text(box, text):
    '''往框里填内容：单行框和多行框的接口不一样'''

    if isinstance(box, QLineEdit):
        box.setText(text)
    else:
        box.setPlainText(text)

# 助手提示词：界面控件名 -> get_prmpt() 里 assistant_prompt 的下标
ASSI_FIELDS = (
    ("assiProfileEdit", 0),     # 基础设定
    ("styleEdit", 1),           # 说话风格
    ("personality", 2),         # 性格特点
)

# 用户基础信息：界面控件名 -> JSON 里的键
BASE_FIELDS = (
    ("userNameEdit", "名字"),
    ("userNicknameEdit", "称呼"),
    ("userGenderEdit", "性别"),
    ("userAgeEdit", "年龄"),
    ("userBirthdayEdit", "生日"),
    ("userIdentityEdit", "身份"),
)


class SettingsPage:
    '''第二页的逻辑，构造函数收一个主窗口（用它的 toast 和翻页）'''

# ====================初始化====================

    def __init__(self, window):
        self.window = window
        self.ui = window.ui
        self._snapshot = {}     # 进页面时的原始内容，用来判断有没有改过
        self._base_raw = []     # 「基础信息」那条的原始结构，保存时要原样还回去

        self._boxes = [getattr(self.ui, name) for name, _ in ASSI_FIELDS]
        self._boxes += [getattr(self.ui, name) for name, _ in BASE_FIELDS]
        self._boxes.append(self.ui.otherEdit)

        # 每次变动都重新比对一遍（改回去就再变灰）
        for box in self._boxes:
            box.textChanged.connect(self._refresh_state)

        # 三个按钮
        self.ui.promptSave.clicked.connect(self.save)
        self.ui.promptCancel.clicked.connect(self.cancel)
        self.ui.PromptClose.clicked.connect(self.close_page)

        self.ui.promptSave.setToolTip("保存当前的设定")

# ====================读写数据库====================

    def load(self):
        '''把数据读进来填好，并记下这次的原始内容'''

        data = prmpt.get_prmpt()
        self._snapshot = {}

        # 助手的三条
        for name, index in ASSI_FIELDS:
            item = data["assistant_prompt"][index]
            self._fill(getattr(self.ui, name), item["text"], item["description"], name)

        # 用户的基础信息（存的是 JSON 列表，每项一个键加一句说明）
        self._base_raw = data["user_prompt"][0]["text"]
        values, descriptions = {}, {}
        for item in self._base_raw:
            for key, value in item.items():
                if key == "description":
                    continue
                values[key] = value
                descriptions[key] = item.get("description", "")
        for name, key in BASE_FIELDS:
            self._fill(getattr(self.ui, name), values.get(key, ""), descriptions.get(key, ""), name)

        # 用户的其他设定
        other = data["user_prompt"][1]
        self._fill(self.ui.otherEdit, other["text"], other["description"], "otherEdit")

        self._refresh_state()

    def _fill(self, box, text, description, key):
        '''填内容：空的就把 description 当灰色占位文字'''

        box.blockSignals(True)      # 填的时候别触发「有改动」
        _set_text(box, text or "")
        box.setPlaceholderText(description or "")
        box.blockSignals(False)

        self._snapshot[key] = text or ""

# ====================判断有没有改动====================

    def _values(self):
        '''把界面上现在的内容取出来'''

        values = {name: _text_of(getattr(self.ui, name)) for name, _ in ASSI_FIELDS}
        values.update({name: _text_of(getattr(self.ui, name)) for name, _ in BASE_FIELDS})
        values["otherEdit"] = _text_of(self.ui.otherEdit)
        return values

    def is_dirty(self):
        '''和进页面时的内容比一比（所以改回去就又不算改过了）'''

        return self._values() != self._snapshot

    def _refresh_state(self):
        '''有改动才让保存键亮起来，没改动就灰掉（灰掉自然点不动也没悬停）'''

        self.ui.promptSave.setEnabled(self.is_dirty())

    # ====================三个按钮====================

    def save(self):
        '''保存：写回数据库 -> 弹个两秒的小提示 -> 回第一页'''

        prmpt.edit_prmpt(*self._collect())
        self.window.show_toast("保存成功！")
        self.load()             # 重新读一遍，快照跟着更新
        self._leave()

    def cancel(self):
        '''取消：有改动才问一句，确认了就把改动丢掉回第一页'''

        if not self.is_dirty():
            self._leave()
            return

        # 下标 1 是「确认」，也就是放弃修改，算危险操作
        index = InfoDialog.ask(self.window, "确认取消？",
                               "当前的修改还没有保存，确定要放弃吗？", ["取消", "确认"], danger=1)
        if index == 1:
            self._leave()

    def close_page(self):
        '''关闭：有改动就给三个选项（取消 / 丢弃 / 保存）'''

        if not self.is_dirty():
            self._leave()
            return

        # 下标 1 是「丢弃」，同样是危险操作
        index = InfoDialog.ask(self.window, "未保存的更改",
                               "你对设定做了修改，想怎么处理？", ["取消", "丢弃", "保存"], danger=1)
        if index == 1:
            self._leave()
        elif index == 2:
            self.save()

    def _collect(self):
        '''把界面上的内容整理成 edit_prmpt 要的两份列表'''

        data = prmpt.get_prmpt()    # 标签名从库里取，只取一次

        assi = []
        for name, index in ASSI_FIELDS:
            assi.append({"label": data["assistant_prompt"][index]["label"],
                         "text": _text_of(getattr(self.ui, name))})

        # 基础信息要把原来那套结构（键 + description）留着，只换值
        # 这里的键要和 JSON 里的键一致（名字、称呼…），下面才是按键取值
        now = {key: _text_of(getattr(self.ui, name)) for name, key in BASE_FIELDS}
        base = []
        for item in self._base_raw:
            new_item = {}
            for key, value in item.items():
                new_item[key] = value if key == "description" else now.get(key, value)
            base.append(new_item)

        user = [
            {"label": data["user_prompt"][0]["label"],
             "text": json.dumps(base, ensure_ascii=False)},      # 数据库里存的是 JSON 字符串
            {"label": data["user_prompt"][1]["label"],
             "text": _text_of(self.ui.otherEdit)},
        ]
        return assi, user

    def _leave(self):
        '''回第一页，顺便把页面内容复位成数据库里的样子'''

        self.load()
        self.window.go_page(0)
