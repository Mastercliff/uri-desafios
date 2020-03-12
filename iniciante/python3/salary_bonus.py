NOME,SALARIO,VENDAS = input(), float(input()), float(input())
VALOR = VENDAS * 0.15
SALARIOFINAL = SALARIO + VALOR
print("TOTAL = R$ %.2f" % SALARIOFINAL)