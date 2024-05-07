n = int(input('Quantos reais você tem? R$'))

d = 5.07


compra = n / d

cF = round(compra, 2)

print('Você tem R${}, pode comprar ${}'.format(n, cF))

