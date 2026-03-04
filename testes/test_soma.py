import unittest
from Calculadora.calculadora import Calculadora

class TestSoma(unittest.TestCase):

    def setUp(self):
        self.c = Calculadora()

    def test_soma_simples(self):
        self.assertEqual(self.c.somar(10, 5), 15)

    def test_soma_negativos(self):
        self.assertEqual(self.c.somar(-10, -5), -15)

    def test_soma_decimais(self):
        self.assertAlmostEqual(self.c.somar(1.5, 2.3), 3.8)

if __name__ == "__main__":
    unittest.main()