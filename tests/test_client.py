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


if __name__ == '__main__':
    unittest.main()
