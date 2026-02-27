🧮 Calculadora em Python com Testes e Interface Gráfica

Projeto de uma Calculadora em Python com:

✅ Operações matemáticas básicas

✅ Validação de entrada

✅ Tratamento de erros

✅ Testes automatizados com unittest

✅ Interface gráfica usando tkinter

📌 Funcionalidades

A classe Calculadora possui os seguintes métodos:

somar(a, b)

subtrair(a, b)

multiplicar(a, b)

dividir(a, b)

✔ Validações implementadas

Aceita apenas números (int ou float)

Impede divisão por zero

Lança erro para entradas inválidas

🗂 Estrutura do Projeto
📁 projeto-calculadora
│
├── calculadora.py        # Classe principal da calculadora
├── test_calculadora.py   # Testes automatizados
├── interface.py          # Interface gráfica com tkinter
└── README.md             # Documentação do projeto
🛠 Tecnologias Utilizadas

Python 3

unittest (testes automatizados)

tkinter (interface gráfica)

▶ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone <seu-repositorio>
cd projeto-calculadora
2️⃣ Executar a Interface Gráfica
python interface.py

A calculadora abrirá em uma janela.

📌 Para usar:
Digite dois números separados por espaço.

Exemplo:

10 5

Depois clique na operação desejada (+, -, *, /).

3️⃣ Executar os Testes Automatizados
python -m unittest test_calculadora.py

Se tudo estiver correto, todos os testes passarão ✅

🧪 Testes Implementados

Os testes cobrem:

Operações básicas

Números negativos

Zero

Números decimais

Valores grandes

Entradas inválidas

Divisão por zero

🚀 Melhorias Futuras

Adicionar botões numéricos na interface

Melhorar layout visual

Histórico de operações

Suporte a mais operações (potência, raiz, etc.)

👨‍💻 Autor

Matheus Carvalho

Projeto desenvolvido para prática de:

Programação Orientada a Objetos

Testes Automatizados

Interface Gráfica em Python
