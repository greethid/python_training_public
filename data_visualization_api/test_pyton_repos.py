import unittest
import python_repos


class NamesTestCase(unittest.TestCase):
    """Test for python_repos.py program"""

    def test_status_code(self):
        """Check if status code is equal 200"""
        self.assertEqual(200, python_repos.r.status_code)