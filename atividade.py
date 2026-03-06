# ---------------------------------------------------------
    # Parte 1 — Compreendendo o que é um teste
    # ---------------------------------------------------------

# 1) O que significa testar uma função em programação?
# Resposta: Significa se a função está funcionando de acordo com o esperado, ou seja, se ela retorna os resultados corretos para as entradas fornecidas.
# 2) Se uma função recebe a expressão '2+3', qual resultado você espera que ela retorne?
# Resposta: O resultado da conta será 5 pois 2+3=5.
# 3) Se quisermos verificar automaticamente se o resultado está correto,
 # qual comando do unittest podemos usar?
# Rwesposta: o comando recomendado é o assertEqual porque ele compara o resultado esperado com o resultado real da função, e se eles forem iguais, o teste passa; caso contrário, ele falha.

# 4) Complete a instrução abaixo para verificar se o resultado é 5:
# Código:
import unittest

from Calculadora.calculadora import Calculadora


def test_soma_2_3(self):
    self.assertEqual(self.c.somar(2,3), 5)
# Resposta: teste passará se a soma for 5


    # Parte 2 — Estrutura de um teste
    # 5) Todo teste unitário possui três partes principais. Quais são elas?
    # Código: Cenário, Execução, Verificação
    # Resposta: define input, chama função e verifica resultado

    # 6) Observe o código abaixo e identifique Cenário, Execução e Verificação:
    # Código:
    # expressao = '3*5'         # Cenário
    # resultado = calcular_expressao(expressao)  # Execução
    # self.assertEqual(resultado, 15)           # Verificação
    # Resposta: verifica que 3*5 retorna 15

    # 7) Teste para verificar se a calculadora resolve 4 + 6 = 10
    # Código:
    def test_soma_4_6(self):
        a = 4   # Cenário
        b = 6   # Cenário
        resultado = self.c.somar(a, b)  # Execução
        self.assertEqual(resultado, 10)  # Verificação
        # Resposta: soma correta

    # Parte 3 — Criando novos testes
    # 8) Crie um teste para verificar 10 - 3 = 7
    def test_subtracao_10_3(self):
        self.assertEqual(self.c.subtrair(10, 3), 7)
        # Resposta: subtração correta

    # 9) Teste multiplicação 7 * 8 = 56
    def test_multiplicacao_7_8(self):
        self.assertEqual(self.c.multiplicar(7, 8), 56)
        # Resposta: multiplicação correta

    # 10) Teste divisão 20 / 5 = 4.0
    def test_divisao_20_5(self):
        self.assertEqual(self.c.dividir(20, 5), 4.0)
        # Resposta: divisão correta

    # Parte 4 — Pensamento crítico
    # 11) O que deveria acontecer se o usuário tentar dividir um número por zero? Ex: 10 / 0
    # 12) Crie teste para verificar
    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.c.dividir(10, 0)
        # Resposta: deve lançar ValueError

    # 13) O que acontece se digitar algo que não é uma expressão válida? Ex: 'abc'
    # 14) Crie teste para verificar
    def test_entrada_invalida(self):
        with self.assertRaises(ValueError):
            self.c.somar("abc", 5)
        # Resposta: deve lançar ValueError

    # Parte 5 — Raciocínio mais avançado
    # 15) A calculadora deve respeitar precedência matemática. Qual resultado 2 + 3 * 4?
    def test_precedencia_matematica(self):
        self.assertEqual(self.c.calcular_expressao('2 + 3 * 4'), 14)
        # Resposta: multiplicação antes da soma

    # 16) Agora teste uma expressão com parênteses: (2 + 3) * 4
    def test_parenteses(self):
        self.assertEqual(self.c.calcular_expressao('(2 + 3) * 4'), 20)
        # Resposta: parênteses respeitados

    # 19) Como testar várias expressões usando um único método de teste?
    def test_varias_expressoes(self):
        casos = [
            ('1 + 1', 2),
            ('2 * 3', 6),
            ('10 - 4', 6),
            ('8 / 2', 4.0),
            ('(3 + 2) * 5', 25)
        ]
        for expressao, esperado in casos:
            with self.subTest(expressao=expressao):
                self.assertEqual(self.c.calcular_expressao(expressao), esperado)
                # Resposta: cada expressão retorna o valor esperado

if __name__ == "__main__":
    calc = Calculadora()

    print("Resultado 1:", calc.somar(10, 5))
    print("Resultado 2:", calc.subtrair(10, 5))
    print("Resultado 3:", calc.multiplicar(10, 5))
    print("Resultado 4:", calc.dividir(10, 5))

    # Testando erro
    try:
        print("Resultado 5:", calc.dividir(10, 0))
    except ValueError as e:
        print("Erro:", e)

    try:
        print("Resultado 6:", calc.somar("a", 5))
    except ValueError as e:
        print("Erro:", e)

        # ---------------------------------------------------------
# Resultados esperados
# ---------------------------------------------------------

# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2.0

# Teste de erro:
# 10 / 0 -> Erro: Divisão por zero não é permitida

# Teste de entrada inválida:
# "a" + 5 -> Erro: Somente números são aceitos