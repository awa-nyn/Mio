'''状态监视：后台轮询服务状态 + 一直盯着网络

- 正常（200 空闲中，绿）60 秒轮询一次；异常每 10 秒一次
- 工具调用（201）时暂停轮询、显示「工作中」（蓝），回到 200 再自动放开
- 另开一个线程一直探网络，断了就显示「无网络」（深灰）
- 标题栏和状态栏两处状态一起刷

stat.status() 是阻塞的（走网络），所以轮询和探网都在子线程里做，
界面线程只收信号，不会被卡住。
'''

import socket
import time

from PySide6.QtCore import QObject, QThread, Signal

POLL_OK = 60        # 状态正常时的轮询间隔（秒）
POLL_BAD = 10       # 状态异常时的轮询间隔（秒）
TICK = 200          # 每 200 毫秒醒一次，好让暂停/退出能立刻生效
NET_TIMEOUT = 1.5   # 探网络时每个目标等多久
NET_ONLINE = 4      # 有网时多久探一次
NET_OFFLINE = 2     # 没网时探得勤一点

# 探网络用的目标（国内的公共 DNS，稳）
NET_TARGETS = (("223.5.5.5", 53), ("114.114.114.114", 53), ("www.baidu.com", 443))


def _load_stat():
    '''把 status 里的 stat 拿回来

    放在函数里是为了「延后导入」：status.py 模块一导入就会发一次网络请求，
    直接写在文件顶部会把界面启动卡住。
    '''

    from GUI.status import stat
    return stat


class StatusWorker(QThread):
    '''后台轮询服务状态'''

    changed = Signal(int)       # 状态码变了就发一次

    def __init__(self, stat_getter=_load_stat, parent=None):
        super().__init__(parent)
        self._get_stat = stat_getter
        self._stop = False

    def stop(self):
        self._stop = True

    def run(self):
        try:
            stat = self._get_stat()
        except Exception as exc:
            print(f"状态监视启动失败：{exc}")
            return

        last_code = None
        last_poll = 0.0

        while not self._stop:
            code = stat.status_code

            if code == 201:
                # 工具调用中：不轮询，就等着它变回 200
                if last_code != 201:
                    last_code = 201
                    self.changed.emit(201)
                self.msleep(TICK)
                continue

            interval = POLL_OK if code == 200 else POLL_BAD
            need_poll = (last_code is None                    # 还没查过
                         or last_code == 201                  # 刚从工具调用回来：马上查一次
                         or time.monotonic() - last_poll >= interval)
            if need_poll:
                try:
                    stat.status()
                except Exception as exc:
                    print(f"状态查询出错：{exc}")
                last_poll = time.monotonic()
                code = stat.status_code if stat.status_code is not None else 0
                if code != last_code:
                    last_code = code
                    self.changed.emit(code)

            self.msleep(TICK)


class NetWorker(QThread):
    '''一直探网络：通就不吭声，断了就发一次 False'''

    changed = Signal(bool)      # True 有网 / False 没网

    def __init__(self, targets=NET_TARGETS, parent=None):
        super().__init__(parent)
        self._targets = targets
        self._stop = False

    def stop(self):
        self._stop = True

    def _online(self):
        '''能连上任意一个目标就算有网'''

        for host, port in self._targets:
            if self._stop:
                return True         # 正在退出就别再等了
            try:
                socket.create_connection((host, port), timeout=NET_TIMEOUT).close()
                return True
            except OSError:
                continue
        return False

    def run(self):
        last = None
        while not self._stop:
            online = self._online()
            if online != last:
                last = online
                self.changed.emit(online)
            self.msleep(NET_ONLINE if online else NET_OFFLINE)


class StatusMonitor(QObject):
    '''把状态画到界面上（标题栏和状态栏各一处）'''

    def __init__(self, window):
        super().__init__(window)
        self.ui = window.ui
        self._code = None
        self._tool_running = False
        self._offline = False

        self.worker = StatusWorker(parent=self)
        self.worker.changed.connect(self.on_code)
        self.worker.start()

        self.net_worker = NetWorker(parent=self)
        self.net_worker.changed.connect(self.on_network)
        self.net_worker.start()

        self._refresh()     # 第一个状态回来之前先显示「加载中」（浅灰）

    # ==========信号处理==========
    def on_code(self, code):
        '''服务状态变了'''

        self._code = code
        self._tool_running = (code == 201)
        self._refresh()

    def on_network(self, online):
        '''网络变了（这个才是实时的）'''

        self._offline = not online
        self._refresh()

    def stop(self):
        '''退出前把两个线程收掉'''

        self.worker.stop()
        self.net_worker.stop()
        for thread in (self.worker, self.net_worker):
            if not thread.wait(1500):
                thread.terminate()      # 万一卡在网络请求上，只能强行收
                thread.wait(500)

    # ==========画到界面上==========
    def _refresh(self):
        '''把当前该显示的状态刷到标题栏和状态栏'''

        if self._offline or self._code == 503:
            state, text, tip = "offline", "无网络", "网络连接异常"
        elif self._code is None:
            state, text, tip = "loading", "加载中", "正在获取服务状态"
        elif self._tool_running:
            state, text, tip = "work", "工作中", "正在调用工具"
        elif self._code == 200:
            state, text, tip = "ok", "空闲中", "服务状态正常"
        else:
            state, text, tip = "error", "异常", f"状态码 {self._code}"

        for label, dot in ((self.ui.statusLabel, self.ui.statusDot),
                           (self.ui.statusLabelBottom, self.ui.statusDotBottom)):
            label.setText(text)
            label.setToolTip(tip)
            dot.setToolTip(tip)
            for widget in (label, dot):
                widget.setProperty("state", state)
                widget.style().unpolish(widget)
                widget.style().polish(widget)
