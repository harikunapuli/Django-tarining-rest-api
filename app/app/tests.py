"""
sample test
"""
from django.test import SimpleTestCase
from app import cal

class calcTests(SimpleTestCase):
    """test calc module"""

    def test_add_numbers(self):
        """test adding numbers together"""
        res = cal.add(5,6)
        self.assertEqual(res, 11)
    def test_subtract_numbers(self):
        """test subtracting numbers"""
        res = cal.subtract(15,10)
        self.assertEqual(res, 5)

