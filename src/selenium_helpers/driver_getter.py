import chromedriver_autoinstaller
from selenium import webdriver


class DriverGetter:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.chromedriver_path = chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
