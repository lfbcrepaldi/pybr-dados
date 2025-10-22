"""Cliente base da API do Senado."""

import requests
from .exceptions import SenadoApiError


class SenadoBaseClient:
    """Cliente base da API do Senado."""

    def __init__(self, base_url: str):
        """Inicializa o cliente com a URL base da API do Senado."""
        self._base_url = base_url

    def _get(self, endpoint: str, params: dict = None) -> list | str:
        """Faz uma requisição GET para a API do Senado.

        Argumentos:
            endpoint (str): O endpoint da API a ser chamado.
            params (dict, optional): Parâmetros a serem enviados na requisição. Padrão:  None.

        Retorno:
            list | str: A resposta da API ou um erro.
        """
        url = f'{self._base_url}/{endpoint}'
        response = requests.get(
            url, params=params, timeout=10, allow_redirects=False
        )  # TODO : Tornar timeout configurável

        self._handle_error(response)

        if (
            'text/csv' in response.headers.get('Content-Type', '') 
            or '.csv' in response.headers.get('content-disposition', '')
        ):
            return response.text
        elif 'application/json' in response.headers.get('Content-Type', ''):
            return response.json()
        return response.text

    def _handle_error(self, response: requests.Response) -> None:
        """Lida com erros da API do Senado.

        Argumentos:
            response (requests.Response): A resposta da requisição.

        Raises:
            SenadoApiError: Se a resposta indicar um erro.
        """
        if not response.ok:
            raise SenadoApiError(
                f'Erro na API do Senado: {response.url} - {response.status_code} - {response.text}'
            )
