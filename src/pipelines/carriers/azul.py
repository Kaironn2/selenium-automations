import requests
from time import sleep

from bs4 import BeautifulSoup

from src.services.gspreads_service import GspreadsService
from utils.dataframe_utils import iso_datetime_to_gsheets_serial # Fix this import


def azul_tracker(order, nfe):

    url = f'https://edi.onlineapp.com.br/Rastreio?chaveNFE={nfe}'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    rows = soup.find_all('tr')

    for row in rows:
        columns = row.find_all('td')

        if len(columns) > 1:
            description = columns[1].text.strip()
            delivery_date = columns[2].text.strip()

            if description.startswith('Remessa entregue'):
                return [order, delivery_date]
        
    return None


def azul_rows_to_track(gspread_service: GspreadsService, sheet_key: str, azul_worksheet: str, edionline_worksheet: str) -> None:

    df = gspread_service.get_worksheet_data(
        sheet_key=sheet_key,
        worksheet_name=azul_worksheet,
    )
    
    ignore_rows = ['ENTREGUE', 'DEVOLUÇÃO', 'DEVOLVIDO', 'EXTRAVIO', 'ERRO']

    df = df[~df['STATUS'].isin(ignore_rows)]

    df = df[(df['NFE'].notna()) & (df['NFE'] != '')]

    total_rows = len(df)
    counter = 0

    for index, row in df.iterrows():

        sleep(1)

        counter += 1

        print(f'Progresso: {counter}/{total_rows}')

        order = row['ORDER']
        nfe = row['NFE']

        data_to_append = azul_tracker(order, nfe)
        print(data_to_append)

        if data_to_append is None:
            continue
        
        order = int(data_to_append[0])
        serialized_date = iso_datetime_to_gsheets_serial(data_to_append[1])
        print(f'Adicionando: {order} - {serialized_date}')


        gspread_service.append_data(
            sheet_key=sheet_key,
            worksheet_name=edionline_worksheet,
            data=[[order, serialized_date]],
        )
