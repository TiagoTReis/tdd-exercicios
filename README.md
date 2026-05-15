# TDD Python — Exercícios Práticos

Projeto desenvolvido para a disciplina de Laboratório, implementando três exercícios com a metodologia **Test-Driven Development (TDD)** em Python.

## Tecnologias

- **Linguagem**: Python 3.12
- **Framework de Testes**: pytest
- **Cobertura de Código**: pytest-cov

## Estrutura do Projeto

```text
tdd-exercicios/
├── exercicio1/
│   ├── __init__.py
│   └── triangulo.py
├── exercicio2/
│   ├── __init__.py
│   └── person.py
├── exercicio3/
│   ├── __init__.py
│   └── calculadora_salario.py
├── tests/
│   ├── test_triangulo.py
│   ├── test_exercicio2.py
│   └── test_exercicio3.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Pré-requisitos

- Python 3.10+
- pip

## Instalação das Dependências

```bash
pip install pytest pytest-cov
```

## Build e Execução dos Testes

### Executar todos os testes

```bash
pytest -v
```

### Executar testes de um exercício específico

```bash
# Exercício 1 - Triângulo
python -m pytest tests/test_triangulo.py -v

# Exercício 2 - Person
python -m pytest tests/test_exercicio2.py -v

# Exercício 3 - Calculadora de Salário
python -m pytest tests/test_exercicio3.py -v
```

### Executar com relatório de cobertura no terminal

```bash
pytest --cov=exercicio1 --cov=exercicio2 --cov=exercicio3 --cov-report=term-missing
```

### Gerar relatório de cobertura em HTML

```bash
pytest --cov=exercicio1 --cov=exercicio2 --cov=exercicio3 --cov-report=html:htmlcov
```

Após executar, abra `htmlcov/index.html` no navegador para ver o relatório detalhado.

---

## Exercícios Implementados

### Exercício 1: Classificação de Triângulos

**Descrição**: lê três valores inteiros representando os lados de um triângulo e informa se é equilátero, isósceles ou escaleno.

**Regras de negócio**:
- Todos os lados devem ser maiores que zero
- A soma de dois lados deve ser estritamente maior que o terceiro lado
- Se os três lados são iguais → Equilátero
- Se exatamente dois lados são iguais → Isósceles
- Se todos os lados são diferentes → Escaleno

**Casos de teste (15 CTs)**:

| CT | Descrição | Entrada | Resultado Esperado |
|----|-----------|---------|-------------------|
| CT01 | Escaleno válido | (3, 4, 5) | ESCALENO |
| CT02 | Isósceles válido | (5, 5, 3) | ISÓSCELES |
| CT03 | Equilátero válido | (6, 6, 6) | EQUILATERO |
| CT04 | Isósceles permutação a==b | (5, 5, 3) | ISÓSCELES |
| CT05 | Isósceles permutação a==c | (5, 3, 5) | ISÓSCELES |
| CT06 | Isósceles permutação b==c | (3, 5, 5) | ISÓSCELES |
| CT07 | Lado zero | (0, 4, 5) | ValueError |
| CT08 | Lado negativo | (-1, 4, 5) | ValueError |
| CT09 | a+b == c | (3, 4, 7) | ValueError |
| CT10 | a+c == b | (3, 7, 4) | ValueError |
| CT11 | b+c == a | (7, 3, 4) | ValueError |
| CT12 | a+b < c | (1, 2, 10) | ValueError |
| CT13 | a+c < b | (1, 10, 2) | ValueError |
| CT14 | b+c < a | (10, 1, 2) | ValueError |
| CT15 | Todos lados zero | (0, 0, 0) | ValueError |

#### Cobertura — Exercício 1

```
Nome                      Stmts   Miss  Cover
---------------------------------------------
exercicio1/triangulo.py      16      0   100%
```

---

### Exercício 2: Validação de Person

**Descrição**: valida um objeto `Person` com nome, idade e lista de e-mails, retornando uma lista de erros.

**Regras de negócio**:
- Nome deve ter ao menos 2 partes e ser composto apenas de letras (acentuação permitida)
- Idade deve estar no intervalo [1, 200]
- Deve haver ao menos um objeto `Email` associado
- Cada email deve estar no formato `usuario@dominio.extensao` com ao menos um caractere em cada parte

**Casos de teste (18 CTs)**

#### Cobertura — Exercício 2

```
Nome                   Stmts   Miss  Cover
------------------------------------------
exercicio2/person.py      43      0   100%
```

---

### Exercício 3: Calculadora de Salário Líquido

**Descrição**: calcula o salário líquido de um funcionário com base no cargo e salário base.

**Regras de desconto**:

| Cargo | Salário Base | Desconto |
|-------|-------------|----------|
| DESENVOLVEDOR | >= R$ 3.000,00 | 20% |
| DESENVOLVEDOR | < R$ 3.000,00 | 10% |
| DBA | >= R$ 2.000,00 | 25% |
| DBA | < R$ 2.000,00 | 15% |
| TESTADOR | >= R$ 2.000,00 | 25% |
| TESTADOR | < R$ 2.000,00 | 15% |
| GERENTE | >= R$ 5.000,00 | 30% |
| GERENTE | < R$ 5.000,00 | 20% |

**Casos de teste (17 CTs)**

#### Cobertura — Exercício 3

```
Nome                                   Stmts   Miss  Cover
-----------------------------------------------------------
exercicio3/calculadora_salario.py         34      0   100%
```

---

## Cobertura Geral do Projeto

```
Name                                Stmts   Miss  Cover
-------------------------------------------------------
exercicio1\__init__.py                  0      0   100%
exercicio1\triangulo.py                16      0   100%
exercicio2\__init__.py                  0      0   100%
exercicio2\person.py                   43      0   100%
exercicio3\__init__.py                  0      0   100%
exercicio3\calculadora_salario.py      34      0   100%
tests\test_exercicio2.py               75      0   100%
tests\test_exercicio3.py               64      0   100%
tests\test_triangulo.py                50      0   100%
-------------------------------------------------------
TOTAL                                 282      0   100%
```

**51 testes — 51 passando — 100% de cobertura**

---

## Metodologia TDD

Cada exercício foi desenvolvido seguindo o ciclo Red → Green → Refactor:

1. **Red**: escrever um teste que falha
2. **Green**: implementar o mínimo de código para o teste passar
3. **Refactor**: melhorar o código mantendo todos os testes passando
