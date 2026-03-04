import tkinter as tk
from .calculadora import Calculadora


class InterfaceCalculadora:

    def __init__(self):
        self.calc = Calculadora()

        self.janela = tk.Tk()
        self.janela.title("Calculadora")
        self.janela.geometry("360x520")
        self.janela.configure(bg="#1e1e1e")
        self.janela.resizable(False, False)

        self.valor_atual = ""
        self.valor_anterior = None
        self.operador = None

        # DISPLAY
        self.display = tk.Entry(
            self.janela,
            font=("Segoe UI", 28),
            bd=0,
            bg="#252526",
            fg="white",
            justify="center"
        )
        self.display.pack(fill="both", padx=15, pady=15, ipady=25)

        # FRAME DOS BOTÕES
        frame = tk.Frame(self.janela, bg="#1e1e1e")
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        botoes = [
            ("7", "#333333"), ("8", "#333333"), ("9", "#333333"), ("÷", "#ff9500"),
            ("4", "#333333"), ("5", "#333333"), ("6", "#333333"), ("×", "#ff9500"),
            ("1", "#333333"), ("2", "#333333"), ("3", "#333333"), ("-", "#ff9500"),
            ("0", "#333333"), (".", "#333333"), ("C", "#a5a5a5"), ("+", "#ff9500"),
            ("=", "#ff9500")
        ]

        linha = 0
        coluna = 0

        for texto, cor in botoes:
            btn = tk.Button(
                frame,
                text=texto,
                font=("Segoe UI", 20),
                bg=cor,
                fg="white",
                bd=0,
                activebackground="#555555",
                command=lambda t=texto: self.clique(t)
            )

            btn.grid(row=linha, column=coluna, sticky="nsew", padx=5, pady=5)

            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        # EXPANSÃO PROPORCIONAL
        for i in range(4):
            frame.columnconfigure(i, weight=1)

        for i in range(5):
            frame.rowconfigure(i, weight=1)

        self.janela.mainloop()

    def clique(self, valor):

        # =====================
        # NÚMEROS E PONTO
        # =====================
        if valor.isdigit() or valor == ".":
            self.valor_atual += valor

            if self.valor_anterior and self.operador:
                self.atualizar_display(
                    f"{self.valor_anterior} {self.operador} {self.valor_atual}"
                )
            else:
                self.atualizar_display(self.valor_atual)

        # =====================
        # OPERADORES
        # =====================
        elif valor in ["+", "-", "×", "÷"]:

            # 👇 TRATAR NEGATIVO NO COMEÇO
            if valor == "-" and self.valor_atual == "" and self.valor_anterior is None:
                self.valor_atual = "-"
                self.atualizar_display(self.valor_atual)
                return

            # 👇 TRATAR NEGATIVO DEPOIS DE OPERADOR
            if valor == "-" and self.valor_atual == "" and self.valor_anterior is not None:
                self.valor_atual = "-"
                self.atualizar_display(
                    f"{self.valor_anterior} {self.operador} {self.valor_atual}"
                )
                return

            # 👇 OPERADOR NORMAL
            if self.valor_atual:
                self.valor_anterior = self.valor_atual
                self.operador = valor
                self.valor_atual = ""

                self.atualizar_display(
                    f"{self.valor_anterior} {self.operador}"
                )

        # =====================
        # IGUAL
        # =====================
        elif valor == "=":

            if self.valor_anterior and self.valor_atual not in ["", "-"]:

                try:
                    n1 = float(self.valor_anterior)
                    n2 = float(self.valor_atual)

                    if self.operador == "+":
                        resultado = self.calc.somar(n1, n2)
                    elif self.operador == "-":
                        resultado = self.calc.subtrair(n1, n2)
                    elif self.operador == "×":
                        resultado = self.calc.multiplicar(n1, n2)
                    elif self.operador == "÷":
                        resultado = self.calc.dividir(n1, n2)

                    expressao = f"{self.valor_anterior} {self.operador} {self.valor_atual} = {resultado}"
                    self.atualizar_display(expressao)

                    self.piscar_resultado()

                    self.valor_atual = str(resultado)
                    self.valor_anterior = None
                    self.operador = None

                except Exception:
                    self.atualizar_display("Erro")
                    self.valor_atual = ""
                    self.valor_anterior = None
                    self.operador = None

        # =====================
        # LIMPAR
        # =====================
        elif valor == "C":
            self.valor_atual = ""
            self.valor_anterior = None
            self.operador = None
            self.atualizar_display("")

    def atualizar_display(self, texto):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, texto)

    def piscar_resultado(self):
        cor_original = self.display.cget("bg")
        self.display.config(bg="#4CAF50")
        self.janela.after(200, lambda: self.display.config(bg=cor_original))


if __name__ == "__main__":
    InterfaceCalculadora()