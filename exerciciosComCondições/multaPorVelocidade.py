Veloc = int(input('Qual a velocidade do carro?: '))

if Veloc <= 80:
    print('Você estava abaixo de 80km/h')
else:
    multa = float((Veloc - 80) * 7)
    print('Você ultrapassou o limite de velocidade e foi multado!')
    print('O valor da multa é de: R${:.2f}'.format(multa))