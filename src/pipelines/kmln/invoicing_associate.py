import os
import json

from src.selenium_helpers.selenium_imports import *


class InvoicingAssociatePipeline(DriverGetter, LoginUtils):
    def __init__(self, collection: str):
        super().__init__()
        self.collection = collection
        self.logger = LoggingUtils(__file__).get_logger()

    def run(self):
        self.login_kmln()
        self.invoicing_url_getter()
        self.collection_filter()
        self.load_invoicing_references()
        input('Remover esse input da pipeline quando for usar')
        self.get_table_data_and_set_input()

    def invoicing_url_getter(self):
        url = os.getenv('KMLN_INVOICING_URL')
        self.driver.get(url)
        self.logger.info(f'Accessing URL: {url}')
    
    def collection_filter(self):
        self.driver.find_element(By.ID, 'colecaoCodigo').send_keys(self.collection)
        self.driver.find_element(By.ID, 'btn-filtrar').click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//tr[@class="success"]'))
        )
        self.logger.info(f'Filter applied: {self.collection}')

    def load_invoicing_references(self):
        invoicing_file = PathUtils.KMLN_DATA_FOLDER / 'invoicing_references.json'
        with open (invoicing_file, encoding='utf-8') as file:
            self.invoicing_references = json.load(file)
        self.logger.info(f'Invoicing references loaded from: {invoicing_file}')

    def get_table_data_and_set_input(self):
        rows = self.driver.find_elements(By.XPATH, '//tr[@class="success"]')
        self.logger.info(f'Found {len(rows)} rows in the table.')

        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            self.logger.info(f'Processing row: {row.text}')
            product_name = columns[4].text.lower()

            for product, reference in self.invoicing_references.items():
                if product in product_name:
                    try:
                        input_ref = columns[11].find_element(By.TAG_NAME, 'input')
                        input_ref.click()
                        input_ref.send_keys(reference)
                        self.logger.info(f'Set reference {reference} for product {product}')
                    except Exception as e:
                        self.logger.error(f'Error setting reference for product {product}: {e}')
                        continue

if __name__ == '__main__':
    driver = InvoicingAssociatePipeline('2025/04/21')
    driver.run()
