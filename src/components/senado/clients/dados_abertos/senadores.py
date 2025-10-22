"""Cliente de API para obter os dados de:
https://adm.senado.gov.br/adm-dadosabertos/swagger-ui/index.html?configUrl=/adm-dadosabertos/swagger-config.json#/Servidores
"""

from .dados_abertos import SenadoDadosAbertosClient
from ...helpers import TipoRetorno

class SenadoresSenadoClient(SenadoDadosAbertosClient):
    """API para dados abertos referentes a servidores, pensionistas, terceirizados e estagiários."""

    def __init__(self):
        """API para dados abertos referentes a servidores, pensionistas, terceirizados e estagiários."""
        super().__init__()
        self._base_url += '/senadores'

    def quantitativos_senadores(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Lista os quantitativos e a distribuição por grupos de Senadores e ex-Senadores que constam da folha de pagamento do Senado Federal.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista dos quantitativos e a distribuição por grupos de Senadores e ex-Senadores.
        """
        url = 'quantitativos/senadores'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def escritorios(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará lista de escritórios de apoio dos senadores.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de escritórios de apoio dos senadores.
        """
        url = 'escritorios'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def despesas_ceaps(self, ano: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retorna uma coleção de despesas CEAPS de todos os senadores do ano especificado.

        Argumentos:
            ano (int): Ano das despesas CEAPS de todos os senadores.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Coleção de despesas CEAPS de todos os senadores do ano especificado.
        """
        url = f'despesas_ceaps/{ano}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def auxilio_moradia(
        self,
        nome_parlamentar: str = None,
        estado_eleito: str = None,
        partido_eleito: str = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON,
    ) -> list | str:
        """Retornará lista de parlamentares indicando se optaram por auxílio moradia e imóvel funcional.

        Argumentos:
            nome_parlamentar (str, optional): Nome do parlamentar. Padrão:  None.
            estado_eleito (str, optional): Estado eleito do parlamentar. Padrão:  None.
            partido_eleito (str, optional): Partido eleito do parlamentar. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de parlamentares indicando se optaram por auxílio moradia e imóvel funcional.
        """
        url = 'auxilio-moradia'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        params = {
            'nomeParlamentarContains': nome_parlamentar,
            'estadoEleitoEquals': estado_eleito,
            'partidoEleitoEquals': partido_eleito,
        }

        return self._get(url, params=params)

    def aposentados(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará lista de senadores aposentados.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de senadores aposentados.
        """
        url = 'aposentados'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)
