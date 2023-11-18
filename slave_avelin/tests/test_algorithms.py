import unittest


from slave_avelin import algorithms as algs
from slave_avelin import typewriters as twrs

class Test_gcd(unittest.TestCase):
    def test_gcd(self):
        twr = twrs.Typewriter()

        self.assertEqual(algs.gcd(25, 15, twr), 5)
        self.assertEqual(algs.gcd(8325974, 93517, twr), 1)
        self.assertEqual(algs.gcd(8325974, 935174, twr), 2)
        self.assertEqual(algs.gcd(7, 7, twr), 7)
        self.assertEqual(algs.gcd(1, 74633423313, twr), 1)
        self.assertEqual(algs.gcd(7364, 1, twr), 1)
        self.assertEqual(algs.gcd(7364, 0, twr), 7364)
        self.assertEqual(algs.gcd(0, 7364, twr), 7364)
        self.assertEqual(algs.gcd(0, 1, twr), 1)
        self.assertEqual(algs.gcd(1, 0, twr), 1)
        self.assertEqual(algs.gcd(0, 0, twr), 0)
    
    def test_gcd_errors(self):
        twr = twrs.Typewriter()

        self.assertRaises(ValueError, algs.gcd, -7364, 1, twr) 
        self.assertRaises(ValueError, algs.gcd, 7364, -341, twr)
        self.assertRaises(ValueError, algs.gcd, -7364, -1, twr)
        self.assertRaises(ValueError, algs.gcd, -7364, 0, twr)
        self.assertRaises(ValueError, algs.gcd, 0, -7364, twr)


