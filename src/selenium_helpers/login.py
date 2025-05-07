import os
from dotenv import load_dotenv
from selenium.webdriver.remote.webdriver import WebDriver


class LoginUtils:
    def __init__(self, driver: WebDriver = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.driver = driver

    def login_kmln(self):
        kmln = os.getenv('KMLN_LOGIN_URL')
        username = os.getenv('KMLN_USERNAME')
        password = os.getenv('KMLN_PASSWORD')
        self.driver.get(kmln)
        self.driver.find_element('id', 'login').send_keys(username)
        self.driver.find_element('id', 'senha').send_keys(password)
        self.driver.find_element('id', 'btnLogin').click()
