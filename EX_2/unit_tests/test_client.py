import sys
sys.path.append('../')
from client import create_presence, process_response_ans
from common.variables import *
import unittest
from errors import ReqFieldMissingError, ServerError


class TestClass(unittest.TestCase):
    """
    Класс с тестами
    """
    def test_def_presense(self):
        """
        Тест коректного запроса
        """
        test = create_presence('Guest')
        test[TIME] = 1.1  # время необходимо приравнять принудительно
        # иначе тест никогда не будет пройден
        self.assertEqual(
            test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        """
        тест корректтного разбора ответа 200
        """
        self.assertEqual(process_response_ans({RESPONSE: 200}), '200 : OK')

    def test_400_ans(self):
        """
        тест корректного разбора 400
        """
        self.assertRaises(
            ServerError, process_response_ans,
            {RESPONSE: 400, ERROR: 'Bad Request'})

    def test_no_response(self):
        """
        тест исключения без поля RESPONSE
        """
        self.assertRaises(
            ReqFieldMissingError, process_response_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
