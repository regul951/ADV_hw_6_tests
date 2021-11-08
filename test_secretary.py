import unittest
from unittest.mock import patch, Mock
from secretary import *


class TestSecretary(unittest.TestCase):

    def test_people_search(self):
        with patch('builtins.input', return_value='10006'):
            expected = people_search()
            result = 'Владелец документа - Аристарх Павлов'
            self.assertEqual(expected, result)

    @patch('builtins.input')
    def test_shelf_search(self, mock_input):
        mock_input.return_value = '11-2'
        expected = shelf_search()
        result = 'Документ 11-2 на полке 1'
        self.assertEqual(expected, result)

    def test_list_of_documents(self):
        expected = list_of_documents()
        result = 'passport 2207 876234 Василий Гупкин'
        self.assertIn(result, expected)
        self.assertEqual(type(expected), type(list()))

    @patch('builtins.input', side_effect=['777', 'metrics', 'Hrun Morjoviy', '1'])
    def test_add_doc(self, input):
        expected = add_doc()
        result = 'Документ metrics добавлен на 1 полку.'
        self.assertEqual(expected, result)


    def test_delete_doc(self):
        with patch('builtins.input', return_value='777'):
            expected = delete_doc()
            result = 'Документ 777 удален.'
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
