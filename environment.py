import os


class Environment:
    DEV = "dev"
    PROD = "prod"

    URLS = {
        DEV: "http://localhost:5000/",
        PROD: "http://localhost:5000/"
    }

    def __init__(self):
        try:
            self.env = os.environ["ENV"]
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Неизвестное занчение ENV переменная {self.env}")


ENV_OBJECT = Environment()
