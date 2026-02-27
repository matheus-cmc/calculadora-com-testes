import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.c = Calculadora()

    # --- Testes básicos ---
    def test_somar(self):
        self.assertEqual(self.c.somar(10, 5), 15)

    def test_subtrair(self):
        self.assertEqual(self.c.subtrair(10, 5), 5)
    
    def test_multiplicar(self):
        self.assertEqual(self.c.multiplicar(10, 5), 50)

    def test_dividir(self):
        self.assertEqual(self.c.dividir(25, 5), 5)

    # --- Testes com números negativos ---
    def test_somar_negativo(self):
        self.assertEqual(self.c.somar(-10, -5), -15)
        self.assertEqual(self.c.somar(-10, 5), -5)

    def test_subtrair_negativo(self):
        self.assertEqual(self.c.subtrair(-10, -5), -5)
        self.assertEqual(self.c.subtrair(-10, 5), -15)

    # --- Testes com zero ---
    def test_zero(self):
        self.assertEqual(self.c.somar(0, 0), 0)
        self.assertEqual(self.c.subtrair(0, 0), 0)
        self.assertEqual(self.c.multiplicar(0, 10), 0)
        with self.assertRaises(ValueError):
            self.c.dividir(10, 0)  # Divisão por zero deve lançar erro

    # --- Testes com números decimais ---
    def test_decimais(self):
        self.assertAlmostEqual(self.c.somar(1.5, 2.3), 3.8)
        self.assertAlmostEqual(self.c.subtrair(5.5, 2.2), 3.3)
        self.assertAlmostEqual(self.c.multiplicar(2.5, 4.0), 10.0)
        self.assertAlmostEqual(self.c.dividir(5.0, 2.0), 2.5)

    # --- Testes com valores grandes ---
    def test_valores_grandes(self):
        self.assertEqual(self.c.somar(10**10, 10**10), 2*10**10)
        self.assertEqual(self.c.multiplicar(10**5, 10**5), 10**10)

    # --- Testes para aceitar apenas números ---
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