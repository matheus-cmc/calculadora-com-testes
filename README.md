# 🧮 Python Calculator — OOP, GUI & Unit Tests

Projeto de uma **Calculadora em Python** com:

- ✅ Programação Orientada a Objetos (POO)
- ✅ Testes automatizados com unittest
- ✅ Interface gráfica com tkinter
- ✅ Validação de entrada
- ✅ Tratamento de erros

---

## 📌 Funcionalidades

A classe `Calculadora` possui os seguintes métodos:

- `somar(a, b)`
- `subtrair(a, b)`
- `multiplicar(a, b)`
- `dividir(a, b)`

### ✔ Validações

- Aceita apenas números (`int` ou `float`)
- Impede divisão por zero
- Lança `ValueError` para entradas inválidas

---

## 🗂 Estrutura do Projeto

```
python-calculator-oop-gui-tests
│
├── calculadora.py
├── test_calculadora.py
├── interface.py
└── README.md
```

---

## ▶ Como Executar

Execute o arquivo da interface:

```bash
python interface.py
```

Para rodar os testes automatizados:

```bash
python -m unittest test_calculadora.py
```

---

## 🧪 Testes Implementados

- Operações básicas  
- Números negativos  
- Zero  
- Números decimais  
- Valores grandes  
- Entradas inválidas  
- Divisão por zero  

---

## 🚀 Melhorias Futuras

- Adicionar botões numéricos  
- Melhorar layout visual  
- Histórico de operações  
- Novas operações (potência, raiz, etc.)  

---

## 👨‍💻 Autor

Matheus Carvalho  

Projeto desenvolvido para prática de:
- Programação Orientada a Objetos  
- Testes Automatizados  
- Interface Gráfica em Python  
