import unittest
from Calculadora.calculadora import Calculadora

class TestEdgeCases(unittest.TestCase):
    def setUp(self):
        # Cria uma instância da calculadora antes de cada teste
        self.c = Calculadora()

    def test_soma_zero(self):
        # Testa a soma de zeros
        self.assertEqual(self.c.somar(0, 0), 0)

    def test_numeros_grandes(self):
        # Testa a soma de números muito grandes
        self.assertEqual(self.c.somar(10**10, 10**10), 2 * 10**10)

    def test_float_precision(self):
        # Testa a precisão de números decimais
        self.assertAlmostEqual(self.c.somar(0.1, 0.2), 0.3, places=1)

    def test_dividir_numero_pequeno(self):
        # Testa a divisão por um número muito pequeno
        self.assertAlmostEqual(self.c.dividir(1, 1e-10), 1e10)

    def test_entrada_errada(self):
        # Testa se a calculadora lança ValueError para entrada inválida
        with self.assertRaises(ValueError):
            self.c.somar("a", 5)

    def test_subtrair_zero(self):
        # Testa a subtração de zeros
        self.assertEqual(self.c.subtrair(0, 0), 0)

    def test_subtrair_negativo(self):
        # Testa subtração de números negativos
        self.assertEqual(self.c.subtrair(-10, -5), -5)

    def test_multiplicar_por_zero(self):
        # Testa multiplicação por zero
        self.assertEqual(self.c.multiplicar(12345, 0), 0)

    def test_multiplicar_grande(self):
        # Testa multiplicação de números grandes
        self.assertEqual(self.c.multiplicar(10**5, 10**5), 10**10)

    def test_divisao_por_zero(self):
        # Testa se a calculadora lança ValueError ao dividir por zero
        with self.assertRaises(ValueError):
            self.c.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
