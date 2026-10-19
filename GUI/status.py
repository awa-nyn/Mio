import openai
from loguru import logger
from client import cli

class Status:
    def __init__(self):
        self.status_code = None

    def status(self):
        '''获取 OpenAI 服务状态与状态码'''

        client: openai.OpenAI = cli.client
        if client:
            try:
                client.models.list()
                if self.status_code != 200:
                    if self.status_code == 503:
                        logger.info("网络已恢复")
                    elif self.status_code is None:
                        logger.info("服务已启动，当前服务状态正常")
                    else:
                        logger.info("服务已恢复")
                    self.status_code = 200    # 空闲中，绿色
            # 以下状态除网络异常外全部显示“异常”，红色
            except openai.APITimeoutError:
                logger.error("请求超时：网络或服务器异常")
                self.status_code = 408    # 请求超时
            except openai.AuthenticationError:
                logger.error("认证错误：API Key无效")
                self.status_code = 401  # API Key错误
            except openai.PermissionDeniedError:
                logger.error("权限错误：API Key无权限访问")
                self.status_code = 403  # API Key无权限访问
            except openai.NotFoundError:
                logger.error("配置错误：Base URL无效或模型不存在")
                self.status_code = 404  # Base URL无效或模型不存在
            except openai.RateLimitError:
                logger.error("请求失败：因请求频率过高被限流或API额度耗尽")
                self.status_code = 429  # 请求频率过高被限流或API额度耗尽
            except openai.InternalServerError:
                logger.error("服务端错误：服务商服务器异常")
                self.status_code = 500  # 服务商服务器异常
            except openai.APIStatusError as e:
                logger.error("其他错误：" + e.message)
                self.status_code = 400  # 其他错误
            except openai.APIConnectionError:
                logger.error("连接错误：网络异常")
                self.status_code = 503  # 网络异常
            except openai.APIError as e:
                logger.error("其他错误：" + str(e))
                self.status_code = 0    # 其他错误
        else:
            logger.error("配置错误：非法的API Key或Base URL")
            self.status_code = 401  # API Key错误

stat = Status()
stat.status()