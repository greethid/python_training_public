"""This module contains unit tests for functions used in english polish dictionary project"""


import unittest
import unittest.mock
from unittest.mock import patch
import re
from resources.english_polish_dictionary import eng_pol_dict, copy_eng_pol_dict
from functions import get_random_word
from functions import start_game
from functions import ask_for_answer
from functions import display_statistics
from functions import reset_game
from functions import hard_reset_game
import functions as f


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
        self.assertEqual('andrzej', f.username)
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
    def test_ask_for_answer_1_to_copy(self, mock_print, mock_input):
        """Checking asking for answer input, special keys: q, s, r and hard reset, correct and incorrect given answer, printing all possible good
        answers, deleting correct answered word from dictionary"""
        answer = ask_for_answer(1)
        mock_input.assert_called_with(f'{answer}: ')

    @patch('builtins.input')
    def test_ask_for_answer_2_first_input(self, mock_input):
        """Checking asking for answer input"""
        answer = ask_for_answer(1)
        mock_input.assert_called_with(f'{answer}: ')

    @patch('builtins.input', return_value='q')
    def test_ask_for_answer_3_q(self, mock_input):
        """Checking special key 'q' """
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', side_effect=['r', 'q'])
    def test_ask_for_answer_4_r_q(self, mock_input):
        """Checking special keys sequence: 'r, q' """
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', side_effect=['s', 'q'])
    def test_ask_for_answer_5_s_q(self, mock_input):
        """Checking special keys sequence: 's, q' """
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', side_effect=['hard reset', 'q'])
    def test_ask_for_answer_6_hard_reset_q(self, mock_input):
        """Checking special keys sequence: 'hard reset, q' """
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', side_effect=['s', 'r', 'r', 'r', 's', 's', 'hard reset', 'hard reset', 's', 'r', 'hard reset', 'r', 'r', 's', 's', 'q'])
    def test_ask_for_answer_7_random_sequence_q(self, mock_input):
        """Checking special keys: random sequence and 'q' finally"""
        answer = ask_for_answer()
        self.assertEqual(answer, 'q')

    @patch('builtins.input', return_value='nikczemny')
    @patch('builtins.print')
    def test_ask_for_answer_8_correct_answer(self, mock_print, mock_input):
        """Checking what happened if correct answer is passed"""
        answer = ask_for_answer(2)
        self.assertEqual(answer, (1, True))
        mock_print.assert_called_with('\x1b[92mOK\x1b[0m')

    @patch('builtins.input', return_value='odpowiedź')
    @patch('builtins.print')
    def test_ask_for_answer_9_incorrect_answer(self, mock_print, mock_input):
        """Checking what happened if incorrect answer is passed"""
        answer = ask_for_answer(2)
        self.assertEqual(answer, (1, False))
        mock_print.assert_called_with('\x1b[91mNOK\x1b[0m')

    @patch('builtins.input', return_value='nikczemny')
    @patch('builtins.print')
    def test_ask_for_answer_10_print_translation(self, mock_print, mock_input):
        """Checking if translation is printed correctly"""
        ask_for_answer(3)
        mock_print.assert_called_with('nikczemny', end=', ')

    @patch('builtins.input', return_value='nikczemny')
    @patch('builtins.print')
    def test_ask_for_answer_11_print_translation_2(self, mock_print, mock_input):
        """Checking if translation is printed correctly"""
        ask_for_answer(4)
        mock_print.assert_called_with('podły')

    @patch('builtins.input', return_value='zła odpowiedź')
    def test_ask_for_answer_12_not_delete_incorrect_answered_word_from_dictionary(self, mock_input):
        """Checking word is not deleted when answer was wrong"""
        length_before = len(eng_pol_dict)
        answer = ask_for_answer(5)
        self.assertEqual('zła odpowiedź', answer)
        self.assertNotIn(answer, eng_pol_dict)
        self.assertIn('abject', eng_pol_dict)
        length_after = len(eng_pol_dict)
        self.assertEqual(length_before, length_after)

    @patch('builtins.input', return_value='nikczemny')
    def test_ask_for_answer_13_delete_correct_answered_word_from_dictionary(self, mock_input):
        """Checking word is deleted when answer was correct"""
        global eng_pol_dict
        length_before = len(eng_pol_dict)
        answer = ask_for_answer(5)
        self.assertEqual('nikczemny', answer)
        self.assertNotIn('abject', eng_pol_dict)
        length_after = len(eng_pol_dict)
        self.assertEqual(length_before - 1, length_after)
        eng_pol_dict = copy_eng_pol_dict.copy()

    @patch('builtins.input', return_value='nikczemny')
    @patch('builtins.print')
    def test_ask_for_answer_14_delete_check_if_all_words_were_answered(self, mock_print, mock_input):
        """Checking what happen if all words were deleted"""
        global eng_pol_dict
        length_before = len(eng_pol_dict)
        answer = ask_for_answer(6)
        length_after = len(eng_pol_dict)
        self.assertEqual(length_before, length_after)
        self.assertIn('abject', eng_pol_dict)
        mock_print.assert_called_with('All words were answered!')

    @patch('builtins.print')
    def test_display_statistics(self, mock_print):
        """Checking is statistics are displayed correctly"""
        display_statistics(1)
        mock_print.assert_called_with(f'Correct answers: 1 out of 2 which is 50 percent.')
        display_statistics()
        mock_print.assert_called_with(f'{len(eng_pol_dict)} words left.')

    @patch('builtins.print')
    def test_stop_game(self, mock_print):
        """Checking set of methods for game ending"""
        display_statistics()
        mock_print.assert_called_with(f'{len(eng_pol_dict)} words left.')

    def test_reset_game(self):
        display_statistics(1)
        self.assertEqual(2, f.all_answers)
        self.assertEqual(1, f.correct_answers)
        reset_game()
        self.assertEqual(0, f.all_answers)
        self.assertEqual(0, f.correct_answers)

if __name__ == '__main__':
    unittest.main()
