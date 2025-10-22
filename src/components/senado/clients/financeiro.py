from ..base_client import SenadoBaseClient
from ..helpers import TipoRetorno


class FinanceiroSenadoClient(SenadoBaseClient):
    def __init__(self):
        """https://www12.senado.leg.br/dados-abertos/conjuntos?portal=Administrativo&grupo=orcamento-do-senado"""
        self._base_url = 'https://www.senado.gov.br/bi-arqs/Arquimedes/Financeiro/'

    def despesas(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> dict:
        """Dados relativos à dotação inicial e final alocada ao Senado Federal nos orçamentos anuais,
        bem como os valores das despesas empenhadas, liquidadas e pagas à conta desses créditos orçamentários..

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de dados desejado. Padrão:  TipoRetorno.JSON.

        Raises:
            ValueError: Tipo de retorno inválido.

        Retorno:
            dict: Dados financeiros do Senado Federal no formato especificado.  
        """
        if tipo_retorno == TipoRetorno.JSON:
            return self._get('DespesaSenadoDadosAbertos.json')
        elif tipo_retorno == TipoRetorno.CSV:
            return self._get('DespesaSenado.csv')
        else:
            raise ValueError("Tipo de retorno inválido. Use 'json' ou 'csv'.")

    def receitas(self, tipo_retorno: TipoRetorno = TipoRetorno.JSON) -> dict:
        """Dados relativos à previsão e à arrecadação de receitas próprias pelo Senado Federal.

        Argumentos:
            tipo_retorno (TipoRetorno, optional): Tipo de dados desejado. Padrão:  TipoRetorno.JSON.

        Raises:
            ValueError: Tipo de retorno inválido.

        Retorno:
            dict: Dados relativos à previsão e à arrecadação de receitas próprias pelo Senado Federal no formato especificado.
        """
        if tipo_retorno == TipoRetorno.JSON:
            return self._get('ReceitasSenadoDadosAbertos.json')
        elif tipo_retorno == TipoRetorno.CSV:
            return self._get('ReceitasSenado.csv')
        else:
            raise ValueError("Tipo de retorno inválido. Use 'json' ou 'csv'.")
