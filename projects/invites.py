from src.selenium_helpers.selenium_imports import *
from selenium.webdriver.support.ui import Select
import pandas as pd
from time import sleep


class InvitesPipeline(DriverGetter, LoginUtils):
    def __init__(self):
        super().__init__()
        self.logger = LoggingUtils(__file__).get_logger()

    def run(self):
        self.login_kmln()
        self.get_url()
        self.company_filter()
        self.date_filter()
        self.get_data()
        sleep(2)
        self.find_data()
        self.save_data()


    def get_url(self):
        url = 'https://erp.kamaleon.com.br/05618295000188/listar.orcamento.do?metodo=listarGet'
        self.driver.get(url)
        self.logger.info(f'Accessing URL: {url}')

    def company_filter(self):
        select_element = self.driver.find_element(By.ID, 'codigoEstabelecimento')
        select = Select(select_element)
        select.select_by_visible_text('02 - COMERCIAL DE CONFECCOES GMM LTDA')

    def date_filter(self, date_str='01/01/2016'):
        date_input = self.driver.find_element(By.ID, 'dataInicial')
        date_input.clear()
        date_input.send_keys(date_str)

    def customer_input(self, customer_name):
        input_cliente = self.driver.find_element(By.ID, 'descricaoCliente')
        input_cliente.clear()
        input_cliente.send_keys(customer_name)
        sleep(2)
        input_cliente.send_keys(Keys.ARROW_DOWN)
        input_cliente.send_keys(Keys.ENTER)

    def filter_button(self):
        filter_button = self.driver.find_element(By.ID, 'btn-filtrar')
        filter_button.click()
        self.logger.info('Filter applied')

    def get_value(self, timeout=10):
        xpath = '//div[@id="totais-status"]//label[contains(text(), "Total Confirmado")]/following-sibling::div/input[@type="text" and @readonly]'
        input_elem = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: \'center\' });", input_elem)
        value = self.driver.execute_script("return arguments[0].value;", input_elem)
        return value

    def get_data(self):
        self.df = pd.read_excel('data.xlsx')
    
    def find_data(self):
        for idx, row in self.df.iterrows():
            self.customer_input(row['cpf'])
            sleep(2)
            self.filter_button()
            sleep(3)
            value = self.get_value()
            self.df.at[idx, 'valor real'] = value
            print(f'Row {idx}: {row["cpf"]} - {value}')
            value = 0
            sleep(2)

    def save_data(self):
        self.df.to_excel('saved_data.xlsx', index=False)

if __name__ == '__main__':
    pipeline = InvitesPipeline()
    pipeline.run()
