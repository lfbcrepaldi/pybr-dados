from .financeiro import FinanceiroSenadoClient
from .dados_abertos import (
    SenadoresSenadoClient,
    ServidoresSenadoClient,
    SupridosSenadoClient,
    ContratacoesSenadoClient
)

__all__ = [
    "FinanceiroSenadoClient",
    "SenadoresSenadoClient",
    "ServidoresSenadoClient",
    "SupridosSenadoClient",
    "ContratacoesSenadoClient",
]