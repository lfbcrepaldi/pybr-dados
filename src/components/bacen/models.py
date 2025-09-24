from __future__ import annotations
from enum import IntEnum, StrEnum
from typing import Any


class SGSCodigoSerie(IntEnum):
    TAXA_CAMBIO_LIVRE_DOLAR_AMERICANO_VENDA_DIARIO = 1
    TAXA_CAMBIO_LIVRE_DOLAR_AMERICANO_VENDA_FIM_PERIODO_ANUAL = 33692
    TAXA_JUROS_SELIC = 11
    TAXA_JUROS_SELIC_ACUMULADA_NO_MES = 4390
    TAXA_JUROS_SELIC_ANUALIZADA_BASE_252 = 1178
    CARTOES_CREDITO_ATIVOS = 25149


class ExpectativasMercadoRelatorio(StrEnum):
    DATAS_REFERENCIA = 'DatasReferencia'
    EXPECTATIVAS_MERCADO_TOP_5_ANUAIS = 'ExpectativasMercadoTop5Anuais'
    EXPECTATIVA_MERCADO_MENSAL = 'ExpectativaMercadoMensais'
    EXPECTATIVAS_MERCADO_TOP_5_INFLACAO_12_MESES = 'ExpectativasMercadoTop5Inflacao12Meses'
    EXPECTATIVAS_MERCADO_INFLACAO_24_MESES = 'ExpectativasMercadoInflacao24Meses'
    EXPECTATIVAS_MERCADO_SELIC = 'ExpectativasMercadoSelic'
    EXPECTATIVAS_MERCADO_TOP_5_SELIC = 'ExpectativasMercadoTop5Selic'
    EXPECTATIVAS_MERCADO_TOP_5_MENSAL = 'ExpectativasMercadoTop5Mensais'
    EXPECTATIVAS_MERCADO_TRIMESTRAIS = 'ExpectativasMercadoTrimestrais'
    EXPECTATIVAS_MERCADO_TOP_5_INFLACAO_24_MESES = 'ExpectativasMercadoTop5Inflacao24Meses'
    EXPECTATIVAS_MERCADO_TOP_5_TRIMESTRAL = 'ExpectativasMercadoTop5Trimestral'
    EXPECTATIVAS_MERCADO_INFLACAO_12_MESES = 'ExpectativasMercadoInflacao12Meses'
    EXPECTATIVAS_MERCADO_ANUAIS = 'ExpectativasMercadoAnuais'


class PTAXRecursos(StrEnum):
    """Tipos de recurso/endpoint para a cotação PTAX.
    Veja detalhes em https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/swagger-ui3#/
    """

    _MOEDAS = 'Moedas'
    _COTACAO_DOLAR_DIA = 'CotacaoDolarDia'
    _COTACAO_DOLAR_PERIODO = 'CotacaoDolarPeriodo'
    _COTACAO_MOEDA_DIA = 'CotacaoMoedaDia'
    _COTACAO_MOEDA_PERIODO = 'CotacaoMoedaPeriodo'
    _COTACAO_MOEDA_ABERTURA_OU_INTERMEDIARIO = 'CotacaoMoedaAberturaOuIntermediario'
    _COTACAO_MOEDA_PERIODO_FECHAMENTO = 'CotacaoMoedaPeriodoFechamento'

    def __call__(self, **kwargs: Any) -> str:
        params = '(' + ','.join(f"{k}='{kwargs[k]}'" for k in kwargs) + ')'
        return f'{self.value}{params}'

    def moedas() -> str:
        """Recurso para listar as moedas disponíveis."""
        return PTAXRecursos._MOEDAS

    def cotacao_dolar_dia(dataCotacao: str) -> str:
        """Recurso para obter a cotação do dólar em um dia específico.

        Args:
            dataCotacao (str): Data da cotação no formato 'MM-DD-YYYY'.
        """
        return PTAXRecursos._COTACAO_DOLAR_DIA(dataCotacao=dataCotacao)

    def cotacao_dolar_periodo(dataInicial: str, dataFinalCotacao: str) -> str:
        """Recurso para obter a cotação do dólar em um período específico.

        Args:
            dataInicial (str): Data inicial no formato 'MM-DD-YYYY'.
            dataFinalCotacao (str): Data final no formato 'MM-DD-YYYY'.
        """
        return PTAXRecursos._COTACAO_DOLAR_PERIODO(dataInicial=dataInicial, dataFinalCotacao=dataFinalCotacao)

    def cotacao_moeda_dia(moeda: str, dataCotacao: str) -> str:
        """Recurso para obter a cotação de uma moeda específica em um dia específico.

        Args:
            moeda (str): Código da moeda (ver recurso Moedas).
            dataCotacao (str): Data da cotação no formato 'MM-DD-YYYY'.
        """
        return PTAXRecursos._COTACAO_MOEDA_DIA(moeda=moeda, dataCotacao=dataCotacao)

    def cotacao_moeda_periodo(codigoMoeda: str, dataInicial: str, dataFinalCotacao: str) -> str:
        """Recurso para obter a cotação de uma moeda específica em um período específico.

        Args:
            codigoMoeda (str): Código da moeda (ver recurso Moedas).
            dataInicial (str): Data inicial no formato 'MM-DD-YYYY'.
            dataFinalCotacao (str): Data final no formato 'MM-DD-YYYY'.
        """
        return PTAXRecursos._COTACAO_MOEDA_PERIODO(codigoMoeda=codigoMoeda, dataInicial=dataInicial, dataFinalCotacao=dataFinalCotacao)
    
    def cotacao_moeda_abertura_ou_intermediario(codigoMoeda: str, dataCotacao: str) -> str:
        """Recurso para obter a cotação de abertura ou intermediária de uma moeda específica em um dia específico.

        Args:
            codigoMoeda (str): Código da moeda (ver recurso Moedas).
            dataCotacao (str): Data da cotação no formato 'MM-DD-YYYY'.
        """
        return PTAXRecursos._COTACAO_MOEDA_ABERTURA_OU_INTERMEDIARIO(codigoMoeda=codigoMoeda, dataCotacao=dataCotacao)

    def cotacao_moeda_periodo_fechamento(codigoMoeda: str, dataInicialCotacao: str, dataFinalCotacao: str) -> str:
        """Recurso para obter a cotação de fechamento de uma moeda específica em um período específico.

        Args:
            codigoMoeda (str): Código da moeda (ver recurso Moedas).
            dataInicialCotacao (str): Data inicial no formato 'MM-DD-YYYY'.
            dataFinalCotacao (str): Data final no formato 'MM-DD-YYYY'.
        """
        return PTAXRecursos._COTACAO_MOEDA_PERIODO_FECHAMENTO(codigoMoeda=codigoMoeda, dataInicialCotacao=dataInicialCotacao, dataFinalCotacao=dataFinalCotacao)
    

