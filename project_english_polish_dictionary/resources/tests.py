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

    @patch('builtins.input', return_value='AndRZej')
    @patch('builtins.print')
    def test_start_game(self, mock_print, mock_input):
        """Checking printing and setting username variable during starting game"""
        print('dupa')
        mock_print.assert_called_with('dupa')
        start_game()
        self.assertEqual('andrzej', functions.username)
        mock_print.assert_called_with('There is no save file for specified user.\nStarting new game.')
        mock_input.assert_called_with('Please type your username and press enter: ')
        start_game(1)
        mock_print.assert_called_with('Welcome to the game for learning English!')
        start_game(2)
        mock_print.assert_called_with('Hello Andrzej!')
        start_game(3)
        mock_print.assert_called_with('Write polish translation for word which you see on the screen and press enter.'
          '\nPress "q" to quit.'
          '\nPress "s" for statistics.'
          '\nPress "r" for reset game.')

    def test_ask_for_answer(self):
        """Checking asking for answer input, special keys: q, s, r and hard reset, correct and incorrect given answer, printing all possible good
        answers, deleting correct answered word from dictionary"""
        pass

# Hello Grzegorz!
# Write polish translation for word which you see on the screen and press enter.
# Press "q" to quit.
# Press "s" for statistics.
# Press "r" for reset game.






if __name__ == '__main__':
    unittest.main()
