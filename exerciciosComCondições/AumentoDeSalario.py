salario = float(input('Qual o salário?: R$'))

if salario > 1250:
    aumento = salario * (10 / 100)
    salComAum = salario + aumento
else:
    aumento = salario * (15 / 100)
    salComAum = salario + aumento
print('O seu novo salário será de: R${:.2f}'.format(salComAum))