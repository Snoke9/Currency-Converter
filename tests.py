import unittest
from unittest.mock import patch
from converter import converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.amount = 100
        self.from_curr = 'EUR'
        self.to_curr = 'RUB'

    @patch('requests.get')
    def test_converter_success(self, mock_get):
        mock_get.return_value.json.return_value = {
            'success': True,
            'result': 9898
        }

        expected_result = f"{self.amount} {self.from_curr.upper()} = 9898 {self.to_curr.upper()}"
        actual_result = converter(self.amount, self.from_curr, self.to_curr)
        self.assertEqual(actual_result, expected_result)

    @patch('requests.get')
    def test_converter_failure(self, mock_get):
        mock_get.return_value.json.return_value = {
            'success': False
        }

        expected_result = "Error: Failed to get data."
        actual_result = converter(self.amount, self.from_curr, self.to_curr)
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
