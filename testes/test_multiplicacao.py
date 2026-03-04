import unittest
from Calculadora.calculadora import Calculadora

class TestMultiplicacao(unittest.TestCase):

    def setUp(self):
        self.c = Calculadora()

    def test_multiplicacao_simples(self):
        self.assertEqual(self.c.multiplicar(10, 5), 50)

    def test_multiplicacao_zero(self):
        self.assertEqual(self.c.multiplicar(0, 10), 0)

    def test_valores_grandes(self):
        self.assertEqual(self.c.multiplicar(10**5, 10**5), 10**10)

if __name__ == "__main__":
    unittest.main()