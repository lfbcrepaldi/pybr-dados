from enum import IntEnum, StrEnum


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
