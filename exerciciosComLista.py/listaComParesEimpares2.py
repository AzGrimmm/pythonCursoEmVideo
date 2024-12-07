numeros = [[],[]]
valor = cont = 0
for n in range(0, 7):
    cont += 1
    valor = int(input(f'Digite o {cont}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-=' * 30)
print(numeros)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')