from datetime import date
import unittest
from unittest.mock import patch
import time

from src.components.senado import (
    FinanceiroSenadoClient,
    TipoRetorno,
    SenadoresSenadoClient,
    ServidoresSenadoClient,
    ContratacoesSenadoClient,
    TipoVinculo,
    Situacao,
    TipoContratacao
)


class TestFinanceiroSenadoClientIntegration(unittest.TestCase):

    def setUp(self):
        self.cliente = FinanceiroSenadoClient()

    def tearDown(self):
        time.sleep(1)  # Para evitar atingir limites de taxa da API

    @patch.object(FinanceiroSenadoClient, '_get')
    def test_despesas_json(self, mock_get):
        mock_get.return_value = [{'resultado': 'ok'}]

        resultado = self.cliente.despesas()
        self.assertEqual(resultado, [{'resultado': 'ok'}])
        mock_get.assert_called_with('DespesaSenadoDadosAbertos.json')

    @patch.object(FinanceiroSenadoClient, '_get')
    def test_despesas_csv(self, mock_get):
        mock_get.return_value = 'resultado,csv\nok,ok'

        resultado = self.cliente.despesas(TipoRetorno.CSV)
        self.assertEqual(resultado, 'resultado,csv\nok,ok')
        mock_get.assert_called_with('DespesaSenado.csv')

    def test_despesas_tipo_invalido(self):
        with self.assertRaises(ValueError):
            self.cliente.despesas(tipo_retorno='xml')


class TestSenadoresSenadoClientIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cliente = SenadoresSenadoClient()

    def tearDown(self):
        time.sleep(1)  # Para evitar atingir limites de taxa da API

    def test_initialization(self):
        self.assertIsInstance(self.cliente, SenadoresSenadoClient)
        self.assertEqual(
            self.cliente._base_url,
            'https://adm.senado.gov.br/adm-dadosabertos/api/v1/senadores'
        )

    def test_quantitativos_senadores_json_integration(self):
        resultado = self.cliente.quantitativos_senadores()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_quantitativos_senadores_csv_integration(self):
        resultado = self.cliente.quantitativos_senadores(TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)

    def test_escritorios_json_integration(self):
        resultado = self.cliente.escritorios()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_escritorios_csv_integration(self):
        resultado = self.cliente.escritorios(TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)

    def test_despesas_ceaps_json_integration(self):
        resultado = self.cliente.despesas_ceaps(2023)
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_despesas_ceaps_csv_integration(self):
        resultado = self.cliente.despesas_ceaps(2023, TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)

    def test_auxilio_moradia_json_integration(self):
        resultado = self.cliente.auxilio_moradia()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_auxilio_moradia_csv_integration(self):
        resultado = self.cliente.auxilio_moradia(tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_aposentados_json_integration(self):
        resultado = self.cliente.aposentados()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_aposentados_csv_integration(self):
        resultado = self.cliente.aposentados(tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)


class TestServidoresSenadoClientIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cliente = ServidoresSenadoClient()

    def tearDown(self):
        time.sleep(1)  # Para evitar atingir limites de taxa da API

    def test_initialization(self):
        self.assertIsInstance(self.cliente, ServidoresSenadoClient)
        self.assertEqual(
            self.cliente._base_url,
            'https://adm.senado.gov.br/adm-dadosabertos/api/v1/servidores'
        )

    def test_servidores_json_integration(self):
        resultado = self.cliente.servidores()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_servidores_with_params_json_integration(self):
        resultado = self.cliente.servidores(
            tipo_vinculo=TipoVinculo.EFETIVO,
            situacao=Situacao.ATIVO,
        )
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_servidores_csv_integration(self):
        resultado = self.cliente.servidores(tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)

    def test_servidores_inativos_integration(self):
        resultado = self.cliente.servidores_inativos()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_servidores_efetivos_integration(self):
        resultado = self.cliente.servidores_efetivos()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_servidores_comissionados_integration(self):
        resultado = self.cliente.servidores_comissionados()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_servidores_ativos_integration(self):
        resultado = self.cliente.servidores_ativos()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_remuneracoes_json_integration(self):
        resultado = self.cliente.remuneracoes(2023, 1)
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_remuneracoes_csv_integration(self):
        resultado = self.cliente.remuneracoes(2023, 1, tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_quantitativos_pessoal_json_integration(self):
        resultado = self.cliente.quantitativos_pessoal()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_quantitativos_pessoal_csv_integration(self):
        resultado = self.cliente.quantitativos_pessoal(tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_quantitativos_cargos_funcoes_json_integration(self):
        resultado = self.cliente.quantitativos_cargos_funcoes()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_quantitativos_cargos_funcoes_csv_integration(self):
        resultado = self.cliente.quantitativos_cargos_funcoes(tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_previsao_aposentadoria_json_integration(self):
        resultado = self.cliente.previsao_aposentadoria()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_previsao_aposentadoria_csv_integration(self):
        resultado = self.cliente.previsao_aposentadoria(tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_pensionistas_json_integration(self):
        resultado = self.cliente.pensionistas()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_pensionistas_csv_integration(self):
        resultado = self.cliente.pensionistas(tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_pensionistas_remuneracoes_json_integration(self):
        resultado = self.cliente.pensionistas_remuneracoes(2023, 1)
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)        

    def test_pensionistas_remuneracoes_csv_integration(self):
        resultado = self.cliente.pensionistas_remuneracoes(2023, 1, tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_lotacies_integration(self):
        resultado = self.cliente.lotacoes()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_horas_extras_json_integration(self):
        resultado = self.cliente.horas_extras(2023, 1)
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_horas_extras_csv_integration(self):
        resultado = self.cliente.horas_extras(2023, 1, tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_estagioarios_integration(self):
        resultado = self.cliente.estagiarios()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)

    def test_estagiarios_csv_integration(self):
        resultado = self.cliente.estagiarios(tipo_retorno=TipoRetorno.CSV)
        self.assertIsInstance(resultado, str)
        self.assertGreater(len(resultado), 0)

    def test_cargos_integration(self):
        resultado = self.cliente.cargos()
        self.assertIsInstance(resultado, list)
        self.assertGreater(len(resultado), 0)


class TestContratacoesSenadoClientIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.cliente = ContratacoesSenadoClient()
        cls.tipos_retorno = [TipoRetorno.JSON, TipoRetorno.CSV]

    def tearDown(self):
        time.sleep(1)  # Para evitar atingir limites de taxa da API

    def test_initialization(self):
        self.assertIsInstance(self.cliente, ContratacoesSenadoClient)
        self.assertEqual(
            self.cliente._base_url,
            'https://adm.senado.gov.br/adm-dadosabertos/api/v1/contratacoes'
        )

    def test_pagamentos_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.pagamentos(
                    TipoContratacao.CONTRATOS,
                    3553,
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_empenhos_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.empenhos(
                    TipoContratacao.CONTRATOS,
                    id_contratacao=3553,
                    id_pagamento=2460,
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_documentos_fiscais_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.documentos_fiscais(
                    TipoContratacao.CONTRATOS,
                    3553,
                    2460,
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_itens(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.itens(
                    TipoContratacao.CONTRATOS,
                    3553,
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_garantias_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.garantias(
                    TipoContratacao.CONTRATOS,
                    4312,
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_terceirizados_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.terceirizados(tipo)
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_notas_empenho_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.notas_empenho(tipo_retorno=tipo)
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_menores_aprendizes_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.menores_aprendizes(tipo)
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_licitacoes_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.licitacoes(tipo_retorno=tipo)
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_licitacao_detalhamentos_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.licitacao_detalhamentos(
                    202,
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_empresas_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.empresas(tipo_retorno=tipo)
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_contratos_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.contratos(tipo_retorno=tipo)
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_aditivos_contrato_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.aditivos_contrato(
                    100,
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_contratos_terceirizados_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.contratos_terceirizados(
                    6137,
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_atas_registro_preco_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.atas_registro_preco(
                    tipo_retorno=tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

    def test_ata_registro_preco_acionamentos_integration(self):
        for tipo in self.tipos_retorno:
            with self.subTest():
                resultado = self.cliente.ata_registro_preco_acionamentos(
                    4360,
                    tipo
                )
                if tipo == TipoRetorno.JSON:
                    self.assertIsInstance(resultado, list)
                    self.assertGreater(len(resultado), 0)
                elif tipo == TipoRetorno.CSV:
                    self.assertIsInstance(resultado, str)
                    self.assertGreater(len(resultado), 0)

if __name__ == '__main__':
    unittest.main()
