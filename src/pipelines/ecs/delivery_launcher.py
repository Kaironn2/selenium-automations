import os
from time import sleep
from datetime import datetime
from dateutil.relativedelta import relativedelta

from src.selenium_helpers.selenium_imports import *
from src.services.gspreads_service import GspreadsService


class DeliveryLauncherPipeline(DriverGetter, LoginUtils):
    def __init__(self):
        super().__init__()
        self.logger = LoggingUtils(__file__).get_logger()

    def run(self):
        self.login_ecs()

    def set_date(self, element, date: str, press_enter: bool = False):
        self.driver.execute_script("arguments[0].value = '';", element)
        element.send_keys(date)
        if press_enter:
            element.send_keys(Keys.ENTER)

    def orders_page(self):
        url = os.getenv('ECS_ORDERS_URL')
        self.driver.get(url)
        self.logger.info(f'Accessing URL: {url}')

        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='totalVendas']//h6[text()='Quantidade de vendas']/preceding-sibling::h3")
        ))
        filter_button = self.driver.find_element(By.ID, 'link-pesquisa')
        ActionChains(self.driver).move_to_element(filter_button).click().perform()

        sleep(3)

        period_filter = self.driver.find_element(By.XPATH, '//*[@id="opc-periodo"]')
        ActionChains(self.driver).move_to_element(period_filter).click().perform()

        sleep(3)

        start_date_value = (datetime.today() - relativedelta(months=2)).replace(day=1).strftime('%d/%m/%Y')
        start_date = self.driver.find_element(By.ID, 'data-ini')
        self.set_date(start_date, start_date_value, press_enter=True)

        sleep(3)

        ActionChains(self.driver).move_to_element(filter_button).click().perform()
        self.logger.info('Filter button clicked')

    def search_orders(self, order):
        search_field = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'pesquisa-mini'))
        )
        search_field.clear()
        search_field.send_keys(order)
        search_field.send_keys(Keys.ENTER)
        sleep(1.25)

    def _delivery_button_click(self):
        li_list = self.driver.find_elements(By.CSS_SELECTOR, "li[id^='im_']")
        for el in li_list:
            if 'Informar Entrega' in el.text:
                self.driver.execute_script('arguments[0].scrollIntoView(true);', el)
                ActionChains(self.driver).move_to_element(el).click().perform()
                break

    def delivery_launch(self, delivery_date):
        options_funnel = self.driver.find_element(
            By.CSS_SELECTOR, "div[id^='button-navigate-'] button.button-navigate-funil"
        )
        self.driver.execute_script('arguments[0].scrollIntoView(true);', options_funnel)
        self.driver.execute_script('arguments[0].click();', options_funnel)

        self._delivery_button_click()

        sleep(1)

        date_field = self.driver.find_element(By.ID, 'dataEntregaModal')
        self.set_date(date_field, delivery_date, press_enter=False)
        print('Data de entrega:', delivery_date)
        save_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Salvar')]")
        save_button.click()
