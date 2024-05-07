salario = float(input('Qual o salário?: '))

aumento = salario * (15 / 100)

SalarioComAumento = salario + aumento

print('O salário de R${:.2f}, com aumento de 15%, sobe para R${:.2f}'.format(salario, SalarioComAumento))

