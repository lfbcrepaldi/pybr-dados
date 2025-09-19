import requests
from datetime import date
from typing import Optional, Literal
from .exceptions import BacenAPIError
from .models import SGSCodigoSerie, ExpectativasMercadoRelatorio

class BacenClient:
    """Cliente para acessar a API do Banco Central do Brasil (Bacen)."""

    def sgs(
        self, 
        codigo_serie: SGSCodigoSerie, 
        data_inicial: Optional[date] = None, 
        data_final: Optional[date] = None, 
        ultimos: int | None = None, 
        formato: Literal['json', 'csv'] = 'json'
        
    ) -> dict | str:
        """Consulta séries temporais do SGS (Sistema Gerenciador de Séries Temporais) do Banco Central do Brasil.
        Args:
            codigo_serie (SGSCodigoSerie): Código da série temporal a ser consultada.
            data_inicial (Optional[date], opcional): Data inicial para o filtro. Defaults to None.
            data_final (Optional[date], opcional): Data final para o filtro. Defaults to None.
            ultimos (int | None, opcional): Número de registros mais recentes a serem retornados. Defaults to None.
            formato (Literal['json', 'csv'], opcional): Formato de retorno dos dados. Pode ser 'json' ou 'csv'. Defaults to 'json'.
        """
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

    def expectativas(self, relatorio: ExpectativasMercadoRelatorio, formato: Literal['json', 'xml', 'atom'] =  None, **odata_params) -> dict | str:
        """Consulta dados de expectativas de mercado do Banco Central do Brasil.

        Args:
            relatorio (ExpectativasMercadoRelatorio): Tipo de relatório de expectativas de mercado a ser consultado.
            formato (Literal['json', 'xml', 'atom'], opcional): Formato de retorno dos dados. Pode ser 'json', 'xml' ou 'atom'.
        """
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

    def emissao_moedas_anual(self, **odata_params) -> dict:
        """Consulta dados de emissão anual de moedas do Banco Central do Brasil.

        Args:
            odata_params: Parâmetros OData adicionais para a consulta.
        """
        BASE_URL = 'https://olinda.bcb.gov.br/olinda/servico/mecir_prog_anual_producao/versao/v1/odata/TodosDadosProducao'
        params = {
            **{'$' + k: v for (k, v) in odata_params.items()}
        }

        response = requests.get(BASE_URL, params=params)
        if not response.ok:
            raise BacenAPIError(f'Erro ao acessar API Bacen: {response.status_code}: {response.text}')
        return response.json()