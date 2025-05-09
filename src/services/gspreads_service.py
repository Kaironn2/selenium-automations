from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


class GspreadsService:
    def __init__(self, creds_file: str = 'service_account.json'):
        self.creds_file = creds_file
        self.client = self.authenticate()
        self._sheets_cache = {}

    def authenticate(self) -> gspread.Client:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(self.creds_file, scope)
        client = gspread.authorize(creds)
        return client

    def open_sheet(self, sheet_key: str, worksheet_name: str) -> gspread.Worksheet:
        cache_key = (sheet_key, worksheet_name)
        if cache_key not in self._sheets_cache:
            spreadsheet = self.client.open_by_key(sheet_key)
            worksheet = spreadsheet.worksheet(worksheet_name)
            self._sheets_cache[cache_key] = worksheet
        return self._sheets_cache[cache_key]

    def get_data(self, sheet_key: str, worksheet_name: str, order_column: str, status_column: str, delivery_date_column: str, sys_column: str) -> pd.DataFrame:
        worksheet = self.open_sheet(sheet_key, worksheet_name)
        data = worksheet.get_all_records()
        return pd.DataFrame(data)

    def get_worksheet_data(self, sheet_key: str, worksheet_name: str) -> pd.DataFrame:
        worksheet = self.open_sheet(sheet_key, worksheet_name)
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        return df

    def append_data(self, sheet_key: str, worksheet_name: str, data: list[list]) -> None:
        worksheet = self.open_sheet(sheet_key, worksheet_name)
        worksheet.append_rows(data, value_input_option='USER_ENTERED')

    @staticmethod
    def datetime_to_gs_serial(dt):
        dt = datetime.strptime(dt, '%d/%m/%Y %H:%M')
        epoch = datetime(1899, 12, 30)
        delta = dt - epoch
        return delta.days + (delta.seconds + delta.microseconds / 1e6) / 86400
