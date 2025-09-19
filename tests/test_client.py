import unittest
from unittest.mock import patch, MagicMock
from datetime import date
from src.components.bacen.client import BacenClient
from src.components.bacen.exceptions import BacenAPIError


class TestBacenClient(unittest.TestCase):
    def setUp(self):
        self.client = BacenClient()

    @patch('requests.get')
    def test_sgs_json_default(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'foo': 'bar'}
        mock_get.return_value = mock_response

        result = self.client.sgs(100)
        self.assertEqual(result, {'foo': 'bar'})
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertIn('bcdata.sgs.100/dados', args[0])
        self.assertEqual(kwargs['params']['formato'], 'json')

    @patch('requests.get')
    def test_sgs_csv_format(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.text = 'header\n1,2'
        mock_get.return_value = mock_response

        result = self.client.sgs(200, formato='csv')
        self.assertEqual(result, 'header\n1,2')
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertIn('bcdata.sgs.200/dados', args[0])
        self.assertEqual(kwargs['params']['formato'], 'csv')

    @patch('requests.get')
    def test_sgs_with_dates(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'ok': True}
        mock_get.return_value = mock_response

        di = date(2022, 5, 1)
        df = date(2022, 5, 31)
        result = self.client.sgs(300, data_inicial=di, data_final=df)
        self.assertEqual(result, {'ok': True})
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['dataInicial'], '01/05/2022')
        self.assertEqual(kwargs['params']['dataFinal'], '31/05/2022')

    @patch('requests.get')
    def test_sgs_with_ultimos(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'ultimos': 5}
        mock_get.return_value = mock_response

        result = self.client.sgs(400, ultimos=5)
        self.assertEqual(result, {'ultimos': 5})
        args, kwargs = mock_get.call_args
        self.assertIn('/ultimos/5', args[0])

    @patch('requests.get')
    def test_sgs_error_raises_exception(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status_code = 404
        mock_response.text = 'Not Found'
        mock_get.return_value = mock_response

        with self.assertRaises(BacenAPIError) as ctx:
            self.client.sgs(500)
        self.assertIn('Erro ao acessar API Bacen: 404: Not Found', str(ctx.exception))

    @patch('requests.get')
    def test_sgs_json_and_csv_return_types(self, mock_get):
        # JSON
        mock_response_json = MagicMock()
        mock_response_json.ok = True
        mock_response_json.json.return_value = {'a': 1}
        mock_get.return_value = mock_response_json
        self.assertIsInstance(self.client.sgs(600), dict)

        # CSV
        mock_response_csv = MagicMock()
        mock_response_csv.ok = True
        mock_response_csv.text = 'a,b'
        mock_get.return_value = mock_response_csv
        self.assertIsInstance(self.client.sgs(601, formato='csv'), str)

    @patch('requests.get')
    def test_sgs_params_combination(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'combo': True}
        mock_get.return_value = mock_response

        di = date(2023, 1, 1)
        df = date(2023, 1, 31)
        result = self.client.sgs(
            700, data_inicial=di, data_final=df, ultimos=3, formato='json'
        )
        self.assertEqual(result, {'combo': True})
        args, kwargs = mock_get.call_args
        self.assertIn('/ultimos/3', args[0])
        self.assertEqual(kwargs['params']['dataInicial'], '01/01/2023')
        self.assertEqual(kwargs['params']['dataFinal'], '31/01/2023')
        self.assertEqual(kwargs['params']['formato'], 'json')

    @patch('requests.get')
    def test_expectativas_json_default(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'result': 123}
        mock_get.return_value = mock_response

        result = self.client.expectativas('RelatorioTeste')
        self.assertEqual(result, {'result': 123})
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertIn('RelatorioTeste', args[0])
        self.assertIn('$format', kwargs['params'])
        self.assertIsNone(kwargs['params']['$format'])

    @patch('requests.get')
    def test_expectativas_xml_format(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.text = '<xml>data</xml>'
        mock_get.return_value = mock_response

        result = self.client.expectativas('RelatorioXML', formato='xml')
        self.assertEqual(result, '<xml>data</xml>')
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['$format'], 'xml')

    @patch('requests.get')
    def test_expectativas_atom_format(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.text = '<atom>data</atom>'
        mock_get.return_value = mock_response

        result = self.client.expectativas('RelatorioAtom', formato='atom')
        self.assertEqual(result, '<atom>data</atom>')
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['$format'], 'atom')

    @patch('requests.get')
    def test_expectativas_with_odata_params(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'odata': True}
        mock_get.return_value = mock_response

        result = self.client.expectativas('RelatorioOData', top=10, filter="foo eq 'bar'")
        self.assertEqual(result, {'odata': True})
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['$top'], 10)
        self.assertEqual(kwargs['params']['$filter'], "foo eq 'bar'")

    @patch('requests.get')
    def test_expectativas_error_raises_exception(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status_code = 500
        mock_response.text = 'Internal Server Error'
        mock_get.return_value = mock_response

        with self.assertRaises(BacenAPIError) as ctx:
            self.client.expectativas('RelatorioErro')
        self.assertIn('Erro ao acessar API Bacen: 500: Internal Server Error', str(ctx.exception))

    @patch('requests.get')
    def test_emissao_moedas_anual_default(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'data': [1, 2, 3]}
        mock_get.return_value = mock_response

        result = self.client.emissao_moedas_anual()
        self.assertEqual(result, {'data': [1, 2, 3]})
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        self.assertIn('TodosDadosProducao', args[0])
        self.assertEqual(kwargs['params'], {})

    @patch('requests.get')
    def test_emissao_moedas_anual_with_odata_params(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = True
        mock_response.json.return_value = {'odata': 'yes'}
        mock_get.return_value = mock_response

        result = self.client.emissao_moedas_anual(top=5, filter="ano eq 2023")
        self.assertEqual(result, {'odata': 'yes'})
        args, kwargs = mock_get.call_args
        self.assertEqual(kwargs['params']['$top'], 5)
        self.assertEqual(kwargs['params']['$filter'], "ano eq 2023")

    @patch('requests.get')
    def test_emissao_moedas_anual_error_raises_exception(self, mock_get):
        mock_response = MagicMock()
        mock_response.ok = False
        mock_response.status_code = 400
        mock_response.text = 'Bad Request'
        mock_get.return_value = mock_response

        with self.assertRaises(BacenAPIError) as ctx:
            self.client.emissao_moedas_anual()
        self.assertIn('Erro ao acessar API Bacen: 400: Bad Request', str(ctx.exception))


if __name__ == '__main__':
    unittest.main()
