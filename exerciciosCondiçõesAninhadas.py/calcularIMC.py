peso = float(input('Qual seu peso?: '))
altura = float(input('Qual sua altura?: '))
imc = peso / (altura ** 2)
print('O IMC desta pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Esta pessoa esta em: ABAIXO DO PESO!')
elif imc < 25:
    print('Esta pessoa esta em: PESO IDEAL!')
elif imc < 30:
    print('Esta pessoa esta em: SOBREPESO!')
elif imc < 40:
    print('Esta pessoa esta em: OBESIDADE!')
else:
    print('Esta pessoa esta em: OBESIDADE MÓRBIDA!')