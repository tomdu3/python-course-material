import unittest
import sample

# test functions from sample.py

class TestCheckFloatsEqual(unittest.TestCase):
    def test_check_floats_equal(self):
        # self.assertEqual(sample.check_floats_equal(0.1, 0.099999999999999), True)
        self.assertTrue(sample.check_floats_equal(0.1, 0.099999999999999))

class TestCheckFloatEqual2(unittest.TestCase):
    def test_check_floats_equal2(self):
        self.assertEqual(sample.check_floats_equal2(0.5, 0.499), True)