import unittest
from Calculadora.calculadora import Calculadora

class TestDivisao(unittest.TestCase):

    def setUp(self):
        self.c = Calculadora()

    def test_divisao_simples(self):
        self.assertEqual(self.c.dividir(25, 5), 5)

    def test_divisao_decimal(self):
        self.assertAlmostEqual(self.c.dividir(5, 2), 2.5)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.c.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()