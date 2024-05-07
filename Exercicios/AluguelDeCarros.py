dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos kilômetros rodados? '))

custoPorDia = dias * 60
custoPorKM = km * 0.15

total = custoPorDia + custoPorKM

print('O preço total do aluguel é de: R${:.2f}'.format(total))