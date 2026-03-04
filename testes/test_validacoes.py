import unittest
from Calculadora.calculadora import Calculadora

class TestValidacoes(unittest.TestCase):

    def setUp(self):
        self.c = Calculadora()

    def test_entrada_nao_numerica(self):
        with self.assertRaises(ValueError):
            self.c.somar("a", 5)

        with self.assertRaises(ValueError):
            self.c.subtrair(10, "b")

        with self.assertRaises(ValueError):
            self.c.multiplicar("x", "y")

        with self.assertRaises(ValueError):
            self.c.dividir(10, "zero")

if __name__ == "__main__":
    unittest.main()