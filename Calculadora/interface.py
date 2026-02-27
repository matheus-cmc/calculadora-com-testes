import tkinter as tk
from calculadora import Calculadora

#entrada
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("500x200")

def validar_numero(valor):
    if valor == "":
        return True
    try:
        float(valor)
        return True
    except ValueError:
        return False

entrada = tk.Entry(janela, width= 20, font=("arial", 12))
entrada.grid(row=0, column=0, columnspan=4, padx=1, pady=10)

#função para calcular

calc= Calculadora()
def calcular(operacao):
    try:
        numeros = entrada.get().split()
        a = float(numeros[0])
        b = float(numeros[1])

        if operacao == '+':
            resultado = calc.somar(a, b)
        elif operacao == '-':
            resultado = calc.subtrair(a, b)
        elif operacao == '*':
            resultado = calc.multiplicar(a, b)
        elif operacao == '/':
            resultado = calc.dividir(a, b)

        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Erro")

# Botões de operação
btn_somar = tk.Button(
    janela,
    text="+",
    width=5,
    height=2,
    font=("Arial", 24),
    command=lambda: calcular("+")
)
btn_somar.grid(row=1, column=0, padx=5, pady=5)

btn_subtrair = tk.Button(
    janela,
    text="-",
    width=5,
    height=2,
    font=("Arial", 24),
    command=lambda: calcular("-")
)
btn_subtrair.grid(row=1, column=1, padx=5, pady=5)

btn_multiplicar = tk.Button(
    janela,
    text="*",
    width=5,
    height=2,
    font=("Arial", 24),
    command=lambda: calcular("*")
)
btn_multiplicar.grid(row=1, column=2, padx=5, pady=5)

btn_dividir = tk.Button(
    janela,
    text="/",
    width=5,
    height=2,
    font=("Arial", 24),
    command=lambda: calcular("/")
)
btn_dividir.grid(row=1, column=3, padx=5, pady=5)

#rodar a janela para fechar a calculadora quando eu quiser
janela.mainloop()