import sympy as sp
import matplotlib.pyplot as plt
#criando as funções de custo total e custo médio
def custo_total(x,cf,cv):
    return cf + cv * x
def custo_medio(x,cf,cv):
    return custo_total(x,cf,cv)/x
def calcular_limite(cf, cv):
    x_sym = sp.symbols('x')
    expressao = cf / x_sym + cv
    limite = sp.limit(expressao, x_sym, sp.oo)
    return limite
cf = float(input("digite o custo fixo: "))
cv = float(input("digite o custo variável: "))
x = float(input("digite a quantidade produzida: "))
if x == 0:
    print("A quantidade produzida não pode ser zero.")
else:
    limite = calcular_limite(cf, cv)
    print(f"Conforme a produção cresce infinitamente, o custo médio se aproxima de: {limite}")
    print("O custo total é: ", custo_total(x,cf,cv))
    print("O custo médio é: ", custo_medio(x,cf,cv))

    quantidades = [1, 10, 100, 1000, 10000]
    print("Simulando com diferentes quantidades produzidas:")
    for x_teste in quantidades:
        resultado = custo_medio(x_teste, cf, cv)
        print(f"Quantidade: {x_teste:>7}, Custo Médio: {resultado:.2f}")

    x_valores = list(range(1, 5001))
    y_valores = [custo_medio(qtd, cf, cv) for qtd in x_valores]
    plt.plot(x_valores, y_valores, label="Custo médio")
    plt.axhline(y=cv, color="red", linestyle="--", label="Custo variável (limite)")
    plt.xlabel("Quantidade produzida (x)")
    plt.ylabel("Custo médio")
    plt.title("Convergência do custo médio para o custo variável")
    plt.legend()
    plt.show()
    print(f"\nInterpretação: conforme a empresa aumenta a produção, o custo médio por unidade")
    print(f"cai e se aproxima de R$ {float(limite):.2f} (o custo variável), mas nunca fica abaixo disso.")
    print(f"Isso mostra que, a partir de uma certa escala de produção, ganhar eficiência com volume")
    print(f"tem um limite — o custo fixo já foi todo 'diluído', e o que resta é só o custo por unidade.")