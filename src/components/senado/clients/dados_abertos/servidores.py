"""Cliente de API para obter os dados de: 
https://adm.senado.gov.br/adm-dadosabertos/swagger-ui/index.html?configUrl=/adm-dadosabertos/swagger-config.json#/Senadores
"""
from .dados_abertos import SenadoDadosAbertosClient
from ...helpers import TipoVinculo, Situacao, TipoRetorno


class ServidoresSenadoClient(SenadoDadosAbertosClient):
    """API para dados abertos referentes a servidores, pensionistas, terceirizados e estagiários."""
    def __init__(self):
        super().__init__()
        self._base_url += '/servidores'

    def servidores(
        self,
        tipo_vinculo: TipoVinculo | None = None,
        situacao: Situacao | None = None,
        lotacao: str | None = None,
        cargo: str | None = None,
        tipo_retorno: TipoRetorno = TipoRetorno.JSON,
    ) -> list:
        """Retornará lista de servidores.

        Argumentos:
            tipo_vinculo (TipoVinculo | None, optional): Tipo de vínculo dos servidores. Padrão:  None.
            situacao (Situacao | None, optional): Situação dos servidores. Padrão:  None.
            lotacao (str | None, optional): Lotação dos servidores. Padrão:  None.
            cargo (str | None, optional): Cargo dos servidores. Padrão:  None.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            dict: Lista de servidores.
        """
        url = 'servidores'
        params = {
            'tipoVinculoEquals': tipo_vinculo,
            'situacaoEquals': situacao,
            'lotacaoEquals': lotacao,
            'cargoEquals': cargo,
        }
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url, params)

    def servidores_inativos(self) -> list:
        """Retornará lista de servidores inativos.

        Retorno:
            list: Relação de servidores inativos.
        """
        url = 'servidores/inativos'
        return self._get(url)

    def servidores_efetivos(self) -> list:
        """Retornará lista de servidores efetivos.

        Retorno:
            list: Lista de servidores efetivos.
        """
        url = 'servidores/efetivos'
        return self._get(url)

    def servidores_comissionados(self) -> list:
        """Retornará lista de servidores comissionados.

        Retorno:
            list: Lista de servidores comissionados.
        """
        url = 'servidores/comissionados'
        return self._get(url)

    def servidores_ativos(self) -> list:
        """Retornará lista de servidores ativos.

        Retorno:
            list: Lista de servidores ativos.
        """
        url = 'servidores/ativos'
        return self._get(url)

    def remuneracoes(self, ano: int, mes: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará remuneração dos servidores, para o ano e mês especificado.

        Argumentos:
            ano (int): Ano da remuneração.
            mes (int): Mês da remuneração.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de remunerações ou mensagem de erro.
        """
        url = f'remuneracoes/{ano}/{mes}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def quantitativos_pessoal(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Lista os quantitativos físicos de servidores efetivos, ativos, aposentados e pensionistas.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de quantitativos de servidores ou mensagem de erro.
        """
        url = 'quantitativos/pessoal'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def quantitativos_cargos_funcoes(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Lista os quantitativos de cargos em comissão e funções de confiança do Senado Federal.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de quantitativos de cargos ou mensagem de erro.
        """
        url = 'quantitativos/cargos-funcoes'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def previsao_aposentadoria(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará quantitativo previsto de aposentadorias, por cargo, ano e mês.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de quantitativos de aposentadorias ou mensagem de erro.
        """
        url = 'previsao-aposentadoria'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def pensionistas(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará lista de todos os pensionistas.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de pensionistas ou mensagem de erro.
        """
        url = 'pensionistas'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def pensionistas_remuneracoes(
        self, ano: int, mes: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON
    ) -> list | str:
        """Retornará remuneração dos pensionistas, para o ano e mês especificado.

        Argumentos:
            ano (int): Ano da remuneração.
            mes (int): Mês da remuneração.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de remunerações ou mensagem de erro.
        """
        url = f'pensionistas/remuneracoes/{ano}/{mes}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def lotacoes(self) -> list | str:
        """Retornará lista de lotações.

        Retorno:
            list | str: Lista de lotações ou mensagem de erro.
        """
        url = 'lotacoes'
        return self._get(url)

    def horas_extras(self, ano: int, mes: int, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará lista das horas extras pagas no ano e mês especificados.

        Argumentos:
            ano (int): Ano da remuneração.
            mes (int): Mês da remuneração.
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Lista de horas extras ou mensagem de erro.
        """
        url = f'horas-extras/{ano}/{mes}'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def estagiarios(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> list | str:
        """Retornará relação de estagiários.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de retorno desejado. Padrão:  TipoRetorno.JSON.

        Retorno:
            list | str: Relação de estagiários.
        """
        url = 'estagiarios'
        if tipo_retorno == TipoRetorno.CSV:
            url += '/csv'
        return self._get(url)

    def cargos(self) -> list:
        """Retornará lista de cargos.

        Retorno:
            list: Lista de cargos.
        """
        url = 'cargos'
        return self._get(url)
