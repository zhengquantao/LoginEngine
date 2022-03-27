

class LoginEngineBase:
    def __init__(self):
        pass

    def parse(self, text: str):
        raise NotImplementedError()

    def login(self, *args, **kwargs):
        raise NotImplementedError()


login_engine = LoginEngineBase()


def main(login_engine):
    username = input("please input username>>>")
    password = input("please input password>>>")
    login_engine.login(username, password)
