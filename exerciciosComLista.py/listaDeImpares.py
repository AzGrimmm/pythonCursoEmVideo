lista = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    resp = str(input('Quer continuar?: '))[0].upper()
    if resp in 'N':
        break
print('-=' * 30)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')