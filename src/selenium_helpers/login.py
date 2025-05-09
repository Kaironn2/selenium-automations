import os
from dotenv import load_dotenv
from src.selenium_helpers.selenium_imports import *


class LoginUtils:
    def __init__(self, driver: WebDriver = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        load_dotenv()
        self.driver = driver

    def login_kmln(self):
        url = os.getenv('KMLN_LOGIN_URL')
        username = os.getenv('KMLN_USERNAME')
        password = os.getenv('KMLN_PASSWORD')
        self.driver.get(url)
        self.driver.find_element('id', 'login').send_keys(username)
        self.driver.find_element('id', 'senha').send_keys(password)
        self.driver.find_element('id', 'btnLogin').click()

    def login_ecs(self):
        url = os.getenv('ECS_LOGIN_URL')
        username = os.getenv('ECS_USERNAME')
        password = os.getenv('ECS_PASSWORD')

        self.driver.get(url)

        username_textfield = self.wait.until(
            EC.presence_of_element_located((By.ID, 'usuario'))
        )
        username_textfield.send_keys(username)

        password_textfield = self.driver.find_element(By.ID, 'senha')
        password_textfield.send_keys(password)

        login_button = self.driver.find_element(By.ID, 'loginbtn')
        login_button.click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, 'sidebar-item-inicio'))
        )
