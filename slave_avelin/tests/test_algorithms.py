import unittest


from slave_avelin.algorithms import gcd
from slave_avelin.typewriters import Typewriter, new_indent

class Test_gcd(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(25, 15), 5)
        self.assertEqual(gcd(8325974, 93517), 1)
        self.assertEqual(gcd(8325974, 935174), 2)
        self.assertEqual(gcd(7, 7), 7)
        self.assertEqual(gcd(1, 74633423313), 1)
        self.assertEqual(gcd(7364, 1), 1)
        self.assertEqual(gcd(7364, 0), 7364)
        self.assertEqual(gcd(0, 7364), 7364)
        self.assertEqual(gcd(0, 1), 1)
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(0, 0), 0)
    
    def test_gcd_errors(self):
        Helen = self._get_slave()

        self.assertRaises(ValueError, gcd, -7364, 1) 
        self.assertRaises(ValueError, gcd, 7364, -341)
        self.assertRaises(ValueError, gcd, -7364, -1)
        self.assertRaises(ValueError, gcd, -7364, 0)
        self.assertRaises(ValueError, gcd, 0, -7364)


