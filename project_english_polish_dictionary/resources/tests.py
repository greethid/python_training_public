"""This module contains unit tests for functions used in english polish dictionary project"""


import unittest
import unittest.mock
from unittest.mock import patch
from resources.english_polish_dictionary import eng_pol_dict, copy_eng_pol_dict
from functions import get_random_word
from functions import start_game
import functions

class FunctionsTestCase(unittest.TestCase):
    """Class for tests for functions used in english polish dictionary project"""

    def test_get_random_word(self):
        """Checking if returned random word is from dictionary"""
        for _ in range(100):
            random_word = get_random_word()
            self.assertIn(random_word, eng_pol_dict)

    @patch('builtins.input', return_value='andrzej')
    @patch('builtins.print')
    def test_start_game(self, mock_print, mock_input):
        """Checking printing and setting username variable during starting game"""
        print('dupa')
        mock_print.assert_called_with('dupa')
        start_game()
        self.assertEqual('Andrzej', functions.username)






if __name__ == '__main__':
    unittest.main()
