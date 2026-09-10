from dotenv import load_dotenv
from openai import OpenAI
from openai import APIError
from core import config
from core import ai_client


# 初始化OpenAI API
def client_get():
    try:
        client = OpenAI(
            api_key=config.c.api_key, 
            base_url=config.c.base_url
        )
    except APIError:
        print("API连接失败，请检查网络或API Key配置是否正确")
        exit(1)
    return client

if __name__ == "__main__":
    # 调用chat函数
    try:
        ai_client.chat(client_get())
    except KeyboardInterrupt:
        print("进程终止：强制退出")