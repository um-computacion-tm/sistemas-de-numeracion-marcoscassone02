import unittest
from binario_to_decimal import binario_to_decimal
class TestBinarioDecimal(unittest.TestCase):
    def test_1(self):
        resultado = binario_to_decimal("1")
        self.assertEqual(resultado, 1)
    def test_5(self):
        resultado = binario_to_decimal("101")
        self.assertEqual(resultado, 5)
    def test_10(self):
        resultado = binario_to_decimal("1010")
        self.assertEqual(resultado, 10)
    def test_24(self):
        resultado = binario_to_decimal("11000")
        self.assertEqual(resultado, 24)

if __name__ == '__main__':
    unittest.main()