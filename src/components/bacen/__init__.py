from .client import BacenClient
from .models import SGSCodigoSerie, ExpectativasMercadoRelatorio, PTAXRecursos
from .exceptions import BacenAPIError

_client = BacenClient()

consulta_series_temporais = _client.sgs
expectativas_mercado = _client.expectativas
emissao_moedas_anual = _client.emissao_moedas_anual
ptax = _client.ptax

__all__ = [
    "consulta_series_temporais",
    "expectativas_mercado",
    "emissao_moedas_anual",
    "ptax",
    "SGSCodigoSerie",
    "BacenAPIError",
    "ExpectativasMercadoRelatorio",
    "PTAXRecursos",
]
