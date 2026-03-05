# 🧮 Python Calculator — OOP, GUI & Unit Tests

Projeto de uma **Calculadora em Python** desenvolvida com foco em boas práticas de programação.

O projeto aplica:

- ✅ Programação Orientada a Objetos (POO)
- ✅ Testes automatizados com `unittest`
- ✅ Interface gráfica com `tkinter`
- ✅ Separação entre lógica e interface
- ✅ Tratamento de erros
- ✅ Suporte a números negativos e decimais

---

## 📌 Sobre o Projeto

Este projeto foi estruturado separando:

- **Lógica matemática** → `calculadora.py`
- **Interface gráfica** → `interface.py`
- **Testes automatizados** → `test_calculadora.py`

A interface apenas captura os eventos do usuário e exibe os resultados.  
Toda a regra de negócio fica isolada na classe `Calculadora`.

Isso segue o princípio de **separação de responsabilidades**, deixando o código mais organizado e testável.

---

## ⚙️ Funcionalidades

A classe `Calculadora` possui os seguintes métodos:

- `somar(a, b)`
- `subtrair(a, b)`
- `multiplicar(a, b)`
- `dividir(a, b)`

### ✔ Validações Implementadas

- Aceita apenas números (`int` ou `float`)
- Permite números negativos
- Permite números decimais
- Impede divisão por zero
- Lança `ValueError` para entradas inválidas

---

## 🖥 Interface Gráfica

A interface foi construída utilizando `tkinter` e possui:

- Display centralizado
- Botões organizados em grid responsivo
- Operações básicas (+, -, ×, ÷)
- Suporte a números negativos
- Feedback visual ao calcular (efeito de destaque)
- Botão de limpar (C)

---

## 🗂 Estrutura do Projeto

```
python-calculator-oop-gui-tests
│
├── calculadora.py          # Lógica das operações matemáticas
├── interface.py            # Interface gráfica com tkinter
├── test_calculadora.py     # Testes automatizados
└── README.md
```

---

## ▶ Como Executar

### 🔹 1️⃣ Executar a Interface Gráfica

No terminal, dentro da pasta do projeto, execute:

```bash
 python -m Calculadora.interface
```

A janela da calculadora será aberta.

---

### 🔹 2️⃣ Executar os Testes Automatizados

Para rodar os testes:

```bash
python -m unittest discover
```
### 🔹 3️⃣ Executar o Teste Individual

Para rodar o teste:

```bash
python -m unittest <pasta_do_teste>.<nome_do_arquivo>.<NomeDaClasse>.<nome_do_metodo>
```
obs: precisa colocar o nome do arquivo que deseja testar individualmente. O test_soma foi usado como exemplo.

exemplo:

```bash
python -m unittest testes.test_soma
```

Se todos os testes estiverem corretos, o terminal exibirá:

```
OK
```

Caso haja erro, o `unittest` mostrará qual teste falhou.

---

## 🧪 Testes Implementados

Os testes cobrem:

- Operações básicas
- Números negativos
- Zero
- Números decimais
- Valores grandes
- Entradas inválidas
- Divisão por zero

---

## 🚀 Melhorias Futuras

- Histórico de operações
- Botão +/- dedicado
- Operações avançadas (potência, raiz quadrada)
- Melhorias visuais no layout
- Versão web utilizando Flask ou React
- Empacotamento como executável

---

## 👨‍💻 Autor

**Matheus Carvalho**

Projeto desenvolvido para prática de:

- Programação Orientada a Objetos
- Testes Automatizados
- Separação de responsabilidades
- Desenvolvimento de aplicações desktop com Python
