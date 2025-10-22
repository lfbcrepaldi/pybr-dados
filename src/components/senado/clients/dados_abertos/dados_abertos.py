from ...base_client import SenadoBaseClient


class SenadoDadosAbertosClient(SenadoBaseClient):
    def __init__(self):
        self._base_url = 'https://adm.senado.gov.br/adm-dadosabertos/api/v1'
