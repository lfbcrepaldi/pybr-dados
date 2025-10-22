"""Cliente para dados abertos referentes a suprimento de fundos.
https://adm.senado.gov.br/adm-dadosabertos/swagger-ui/index.html?configUrl=/adm-dadosabertos/swagger-config.json#/Supridos
"""

from .dados_abertos import SenadoDadosAbertosClient
from ...helpers import TipoRetorno


class SupridosSenadoClient(SenadoDadosAbertosClient):
    """Cliente para dados abertos referentes a suprimento de fundos."""
    def __init__(self):
        """Cliente para dados abertos referentes a suprimento de fundos."""
        super().__init__()
        self._base_url += '/supridos'

    def por_ano(self, ano: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará Pessoas supridas por ato de concessão em determinado ano.
        
        Argumentos:
            ano (int): Ano das pessoas supridas.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.
        
        Retorno:
            list | str: Lista de pessoas supridas.
        """
        url = f'{ano}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def transacoes(self, ano: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará lista de transações vinculadas a atos de concessão de um determinado ano.
        
        Argumentos:
            ano (int): Ano das transações.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de transações.
        """
        url = f'transacoes/{ano}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def movimentacoes(self, ano: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará lista de movimentações vinculadas a atos de concessão de um determinado ano.

        Argumentos:
            ano (int): Ano das movimentações.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de movimentações.
        """
        url = f'movimentacoes/{ano}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def empenhos(self, ano: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará lista de empenhos vinculados a atos de concessão de um determinado ano.

        Argumentos:
            ano (int): Ano dos empenhos.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de empenhos.
        """
        url = f'empenhos/{ano}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def atos_concessao(self, ano: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará lista dos Atos de concessão de um determinado ano.

        Argumentos:
            ano (int): Ano dos atos de concessão.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista dos Atos de concessão.
        """
        url = f'atosConcessao/{ano}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)
