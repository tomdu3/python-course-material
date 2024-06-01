'''
Testing calc.py
'''

import unittest
import math
from calc import circle_area, circle_circumference, triangle_area, triangle_check

# Define a test class

class TestCalc(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(circle_area(5), 78.53981633974483)

    def test_circle_circumference(self):
        self.assertEqual(circle_circumference(5), 31.41592653589793)
    
    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(4, 5, 6), 9.92156741649221)

    def test_triangle_check(self):
        self.assertEqual(triangle_check(4, 5, 6), True)
        self.assertEqual(triangle_check(4, 5, 1), False)


if __name__ == "__main__":
    unittest.main()