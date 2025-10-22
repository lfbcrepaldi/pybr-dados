from .clients import (
    SenadoresSenadoClient,
    ServidoresSenadoClient,
    SupridosSenadoClient,
    FinanceiroSenadoClient,
    ContratacoesSenadoClient
)
from .helpers import (
    TipoContratacao,
    TipoRetorno,
    Situacao,
    TipoVinculo
)


senadores = SenadoresSenadoClient()
servidores = ServidoresSenadoClient()
supridos = SupridosSenadoClient()
financeiro = FinanceiroSenadoClient()
contratacoes = ContratacoesSenadoClient()

__all__ = [
    'senadores',
    'servidores',
    'supridos',
    'financeiro',
    'contratacoes',
    'TipoContratacao',
    'TipoRetorno',
    'Situacao',
    'TipoVinculo'
]