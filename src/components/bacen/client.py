import requests
from datetime import date
from typing import Optional, Literal
from .exceptions import BacenAPIError

class BacenClient:
    BASE_URL = 'https://api.bcb.gov.br/dados/serie/'


    def sgs(
        self, 
        codigo_serie: int, 
        data_inicial: Optional[date] = None, 
        data_final: Optional[date] = None, 
        ultimos: int | None = None, 
        formato: Literal['json', 'csv'] = 'json'
    ) -> dict | str:
        params = {
            'formato': formato,
        }
        if data_inicial:
            params['dataInicial'] = data_inicial.strftime('%d/%m/%Y')
        if data_final:
            params['dataFinal'] = data_final.strftime('%d/%m/%Y')

        suffix = f'/ultimos/{ultimos}' if ultimos else ''

        url = f'{self.BASE_URL}bcdata.sgs.{codigo_serie}/dados{suffix}'
        response = requests.get(url, params=params)
        if not response.ok:
            raise BacenAPIError(f'Erro ao acessar API Bacen: {response.status_code}: {response.text}')
        if formato == 'csv':
            return response.text
        return response.json()
