import requests
from lxml import etree

from LoginEngine.engine_base import LoginEngineBase, main


class GithubLoginEngine(LoginEngineBase):
    def __init__(self):
        self.session = requests.session()
        self.headers = {
            'Host': 'github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64;rv:62.0) Gecko/20100101 Firefox/62.0',
        }
        self.login_url = 'https://github.com/login'
        self.profile_url = 'https://github.com/settings/profile'
        self.session_url = 'https://github.com/session'
        super(GithubLoginEngine, self).__init__()

    def parse(self, text: str):
        selector = etree.HTML(text)
        return selector.xpath('//*[@name="authenticity_token"]/@value')

    def login(self, username, password):
        response = self.session.get(url=self.login_url, headers=self.headers)
        print("%s -> %s" % (self.login_url, response.status_code))
        authenticity_token = self.parse(response.text)
        form_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': authenticity_token,
            'login': username,
            'password': password
        }

        response = self.session.post(url=self.session_url, data=form_data, headers=self.headers)
        if response.status_code == 200:
            print("%s -> %s" % (self.session_url, response.status_code))

        response = self.session.get(url=self.profile_url)
        if response.status_code == 200:
            print("%s -> %s" % (self.profile_url, response.status_code))
            self.profile(response.text)

    def profile(self, text):
        pass


if __name__ == '__main__':
    github = GithubLoginEngine()
    main(github)
    # github.login("user", "pwd")
