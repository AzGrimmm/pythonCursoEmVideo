distância = int(input('Qual a distância da viagem em km?: '))

if distância <= 200:
    preço = float(0.50)
    valorPassagem = distância * preço
    print('O valor da sua passagem é de: R${:.2f}'.format(valorPassagem))
else:
    preço = float(0.45)
    valorPassagem = distância * preço
    print('O valor da sua passagem é de: R${:.2f}'.format(valorPassagem))
