import unittest
from Calculadora.calculadora import Calculadora

class TestSubtracao(unittest.TestCase):

    def setUp(self):
        self.c = Calculadora()

    def test_subtracao_simples(self):
        self.assertEqual(self.c.subtrair(10, 5), 5)

    def test_subtracao_negativos(self):
        self.assertEqual(self.c.subtrair(-10, -5), -5)

if __name__ == "__main__":
    unittest.main()