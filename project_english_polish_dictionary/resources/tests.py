"""This module contains unit tests for functions used in english polish dictionary project"""


import unittest
import unittest.mock
from unittest.mock import patch
import re
from resources.english_polish_dictionary import eng_pol_dict, copy_eng_pol_dict
from functions import get_random_word
from functions import start_game
from functions import ask_for_answer
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

    @patch('builtins.input', return_value='answer')
    @patch('builtins.print')
    def test_ask_for_answer_to_copy(self, mock_print, mock_input):
        """Checking asking for answer input, special keys: q, s, r and hard reset, correct and incorrect given answer, printing all possible good
        answers, deleting correct answered word from dictionary"""
        answer = ask_for_answer(1)
        mock_input.assert_called_with(f'{answer}: ')

    @patch('builtins.input')
    def test_ask_for_answer_first_input(self, mock_input):
        """Checking asking for answer input"""
        answer = ask_for_answer(1)
        mock_input.assert_called_with(f'{answer}: ')

    @patch('builtins.input', return_value='q')
    def test_ask_for_answer_q(self, mock_input):
        """Checking special key 'q' """
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', side_effect=['r', 'q'])
    def test_ask_for_answer_r_q(self, mock_input):
        """Checking special keys sequence: 'r, q' """
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', side_effect=['s', 'q'])
    def test_ask_for_answer_s_q(self, mock_input):
        """Checking special keys sequence: 's, q' """
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', side_effect=['hard reset', 'q'])
    def test_ask_for_answer_hard_reset_q(self, mock_input):
        """Checking special keys sequence: 'hard reset, q' """
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', side_effect=['s', 'r', 'r', 'r', 's', 's', 'hard reset', 'hard reset', 's', 'r', 'hard reset', 'r', 'r', 's', 's', 'q'])
    def test_ask_for_answer_random_sequence_q(self, mock_input):
        """Checking special keys: random sequence and 'q' finally"""
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', return_value='nikczemny')
    @patch('builtins.print')
    def test_ask_for_answer_correct_answer(self, mock_print, mock_input):
        """Checking what happened if correct answer is passed"""
        answer = ask_for_answer(2)
        self.assertEqual(answer, (1, True))
        mock_print.assert_called_with('\x1b[92mOK\x1b[0m')

    @patch('builtins.input', return_value='odpowiedź')
    @patch('builtins.print')
    def test_ask_for_answer_incorrect_answer(self, mock_print, mock_input):
        """Checking what happened if incorrect answer is passed"""
        answer = ask_for_answer(2)
        self.assertEqual(answer, (0, False))
        mock_print.assert_called_with('\x1b[91mNOK\x1b[0m')

    @patch('builtins.input', return_value='nikczemny')
    @patch('builtins.print')
    def test_ask_for_answer_print_translation(self, mock_print, mock_input):
        """Checking if translation is printed correctly"""
        ask_for_answer(3)
        mock_print.assert_called_with('nikczemny', end=', ')

    @patch('builtins.input', return_value='nikczemny')
    @patch('builtins.print')
    def test_ask_for_answer_print_translation_2(self, mock_print, mock_input):
        """Checking if translation is printed correctly"""
        ask_for_answer(4)
        mock_print.assert_called_with('podły')

    def test_ask_for_answer_delete_correct_answered_word_from_dictionary(self):
        pass




if __name__ == '__main__':
    unittest.main()
