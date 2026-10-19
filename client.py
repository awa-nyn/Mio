from openai import OpenAI, APIError
from core.config import c


class Client:
    def __init__(self):
        self.client = None

    def client_get(self):
        try:
            self.client = OpenAI(
                api_key=c.api_key, 
                base_url=c.base_url
            )
        except APIError:
            pass

cli = Client()