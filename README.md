# Custo Médio de Produção. Um Problema de Limites

Projeto que aplica o conceito matemático de **limites** para resolver um problema real de **Administração**: como o custo médio por unidade produzida se comporta conforme uma empresa aumenta sua escala de produção.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)

---

## Sobre o problema

Toda empresa possui dois tipos de custo:

- **Custo Fixo (CF)** não muda com a produção (aluguel, máquinas, etc.)
- **Custo Variável (CV)** cresce proporcionalmente a cada unidade produzida (matéria-prima, insumos, etc.)

Quanto mais unidades são produzidas, mais o custo fixo se "dilui" entre elas e o custo médio por unidade se aproxima cada vez mais do custo variável, **sem nunca ficar abaixo dele**. Isso é, na prática, um limite matemático.

## Modelagem matemática

**Custo Total:**

$$CT(x) = CF + CV \cdot x$$

**Custo Médio:**

$$CMe(x) = \frac{CT(x)}{x} = \frac{CF}{x} + CV$$

**O limite que o projeto calcula e comprova:**

$$\lim_{x \to \infty} CMe(x) = CV$$

Conforme $x$ (quantidade produzida) cresce infinitamente, o termo $CF/x$ tende a zero, e o custo médio converge para o custo variável, o "piso" que ele nunca ultrapassa por baixo.

## O que o sistema faz

-  Recebe custo fixo, custo variável e uma quantidade produzida como entrada
-  Calcula o custo total e o custo médio para essa quantidade
-  Calcula o **limite simbólico** da função de custo médio usando `sympy`
-  Simula o custo médio para diferentes quantidades (1, 10, 100, 1.000, 10.000...), mostrando a convergência na prática
- Plota um **gráfico** (matplotlib) da curva de custo médio se aproximando da reta do custo variável
-  Interpreta os resultados no contexto do problema de negócio

##  Como executar

Este projeto usa [uv](https://docs.astral.sh/uv/) como gerenciador de pacotes.

```bash
# Clone o repositório
git clone https://github.com/mateustavaresw/custo-medio-limites.git
cd custo-medio-limites
# Instale as dependências
uv sync
# Execute o programa
uv run main.py
```

Quando solicitado, digite o custo fixo, o custo variável e uma quantidade produzida. O programa vai imprimir os resultados no terminal e abrir uma janela com o gráfico.

## Tecnologias utilizadas

| Tecnologia | Uso no projeto |
|---|---|
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="24"/> **Python** | Linguagem principal |
| **sympy** | Cálculo simbólico do limite matemático |
| **matplotlib** | Visualização gráfica da convergência |
| **uv** | Gerenciamento de dependências e ambiente virtual |
