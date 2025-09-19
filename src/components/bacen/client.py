import requests
from datetime import date
from typing import Optional, Literal
from .exceptions import BacenAPIError
from .models import SGSCodigoSerie, ExpectativasMercadoRelatorio

class BacenClient:

    def sgs(
        self, 
        codigo_serie: SGSCodigoSerie, 
        data_inicial: Optional[date] = None, 
        data_final: Optional[date] = None, 
        ultimos: int | None = None, 
        formato: Literal['json', 'csv'] = 'json'
        
    ) -> dict | str:
        BASE_URL = 'https://api.bcb.gov.br/dados/serie/'

        params = {
            'formato': formato,
        }
        if data_inicial:
            params['dataInicial'] = data_inicial.strftime('%d/%m/%Y')
        if data_final:
            params['dataFinal'] = data_final.strftime('%d/%m/%Y')

        suffix = f'/ultimos/{ultimos}' if ultimos else ''

        url = f'{BASE_URL}bcdata.sgs.{codigo_serie}/dados{suffix}'
        response = requests.get(url, params=params)
        if not response.ok:
            raise BacenAPIError(f'Erro ao acessar API Bacen: {response.status_code}: {response.text}')
        if formato == 'csv':
            return response.text
        return response.json()

    def expectativas(self, relatorio: ExpectativasMercadoRelatorio, formato: Literal['json', 'xml', 'atom'] =  None, **odata_params):
        BASE_URL = f'https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/{relatorio}'
        params = {
            '$format': formato,
            **{'$' + k: v for (k, v) in odata_params.items()}
        }

        response = requests.get(BASE_URL, params=params)
        if not response.ok:
            raise BacenAPIError(f'Erro ao acessar API Bacen: {response.status_code}: {response.text}')
        if formato in ['xml', 'atom']:
            return response.text
        return response.json()
