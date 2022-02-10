"""This module contains unit tests for functions used in english polish dictionary project"""


import unittest
from resources.english_polish_dictionary import eng_pol_dict, copy_eng_pol_dict
from functions import get_random_word


class FunctionsTestCase(unittest.TestCase):
    """Class for tests for functions used in english polish dictionary project"""

    def test_get_random_word(self):
        random_word = get_random_word()
        self.assertIn(random_word, eng_pol_dict)


if __name__ == '__main__':
    unittest.main()
