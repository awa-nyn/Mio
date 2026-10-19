from core import ai_client
import asyncio
from PySide6.QtWidgets import QApplication
from pathlib import Path
import sys
import qasync
from GUI.main_window import MainWindow
from loguru import logger
from client import cli

if getattr(sys, "frozen", False):
    source = Path(sys.executable).parent
else:
    source = Path(__file__).parent


if __name__ == "__main__":
    logger.add(source / "logs" / "app.log", rotation="10 MB", delay=True, retention="7 days", encoding="utf-8")
    logger.add(source / "logs" / "error.log", rotation="10 MB", delay=True, level="ERROR", retention="7 days", encoding="utf-8")
    # logger.add(func, level="INFO", format="{time:HH:mm} - {level:<8} - {message}", rotation="10 MB", retention="7 days", encoding="utf-8")  # 输出到日志界面

    # 共用事件循环
    logger.info("启动应用程序……")

    app = QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)

    logger.info("初始化GUI……")
    window = MainWindow()
    window.show()

    with loop:
        loop.run_forever()

    # 调用chat函数
    try:
        logger.info("启动对话……")
        client = cli.client
        if client:
            ai_client.chat(client)
    except KeyboardInterrupt:
        logger.info("进程终止：强制退出")