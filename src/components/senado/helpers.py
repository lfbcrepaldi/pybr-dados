from enum import StrEnum


class TipoRetorno(StrEnum):
    """Representa o tipo de retorno da API."""

    JSON = "json"
    CSV = "csv"


class TipoVinculo(StrEnum):
    """Representa o tipo de vínculo do servidor."""

    EXERCICIO_PROVISORIO = "EXERCICIO_PROVISORIO"
    COMISSIONADO = "COMISSIONADO"
    REQUISITADO = "REQUISITADO"
    PARLAMENTAR = "PARLAMENTAR"
    EFETIVO = "EFETIVO"


class Situacao(StrEnum):
    """Representa a situação do servidor."""

    ATIVO = "ATIVO"
    INATIVO = "INATIVO"
    DESLIGADO = "DESLIGADO"
    APOSENTADO = "APOSENTADO"


class TipoContratacao(StrEnum):
    """Representa o tipo de contratação."""

    CONTRATOS = "contratos"
    ATAS_REGISTRO_PRECO = "atas_registro_preco"
    NOTAS_EMPENHO = "notas_empenho"
