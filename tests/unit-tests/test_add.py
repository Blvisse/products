import unittest

from scripts.add import quick_addition

class TestAdd(unittest.TestCase):
    def test_add_pd(self):
        result = quick_addition(3,3,3)

        assert result == 9
