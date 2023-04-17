import unittest
from decimal_to_binario import decimal_to_binario
class TestDecimalBinario(unittest.TestCase):
    def test_1(self):
        resultado = decimal_to_binario(1)
        self.assertEqual(resultado, "1")
    def test_5(self):
        resultado = decimal_to_binario(5)
        self.assertEqual(resultado, "101")
    def test_10(self):
        resultado = decimal_to_binario(10)
        self.assertEqual(resultado, "1010")
    def test_24(self):
        resultado = decimal_to_binario(24)
        self.assertEqual(resultado, "11000")

if __name__ == '__main__':
    unittest.main()