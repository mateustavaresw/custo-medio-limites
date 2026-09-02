#criando as funções de custo total e custo médio
def custo_total(x,cf,cv):
    return cf + cv * x
def custo_medio(x,cf,cv):
    return custo_total(x,cf,cv)/x
cf = float(input("digite o custo fixo: "))
cv = float(input("digite o custo variável: "))
x = float(input("digite a quantidade produzida: "))
