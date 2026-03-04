import unittest
from Calculadora.calculadora import Calculadora

class TestEdgeCases(unittest.TestCase):

    def setUp(self):
        self.c = Calculadora()

    def test_soma_zero(self):
        self.assertEqual(self.c.somar(0, 0), 0)

    def test_numeros_grandes(self):
        self.assertEqual(self.c.somar(10**10, 10**10), 2 * 10**10)

    def test_float_precision(self):
        self.assertAlmostEqual(self.c.somar(0.1, 0.2), 0.3, places=1)

if __name__ == "__main__":
    unittest.main()