import signal
# 处理 Ctrl+C 信号
def ctrl_c(signum, frame):
    pass

signal.signal(signal.SIGINT, ctrl_c)

from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError
import os
from core import config
from core.ai_client import chat

# 加载环境变量
if config.get("env"):
    load_dotenv()
    api_key = os.environ.get(config.get("api_key_name"))
else:
    api_key = config.get("api_key")

# 初始化OpenAI API
try:
    client = OpenAI(
        api_key=api_key, 
        base_url=config.get("base_url"))
except APIError:
    print("API连接失败，请检查网络或API Key配置是否正确")
    exit(1)

# 调用chat函数
try:
    chat(client)
except KeyboardInterrupt:
    print("进程终止：强制退出")