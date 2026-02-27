class Calculadora:
    # Função interna para validar entrada
    def _verificar_numeros(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Somente números são aceitos")

    def somar(self, a, b):
        self._verificar_numeros(a, b)
        return a + b

    def subtrair(self, a, b):
        self._verificar_numeros(a, b)
        return a - b

    def multiplicar(self, a, b):
        self._verificar_numeros(a, b)
        return a * b

    def dividir(self, a, b):
        self._verificar_numeros(a, b)
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b