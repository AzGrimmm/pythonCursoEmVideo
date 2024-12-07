numeros = []
cont_pares = cont_impares = cont_numeros = 0
print('=-' * 30)
for n in range(0, 7):
    cont_numeros += 1
    numero = int(input(f'Digite o {cont_numeros}º número: '))
    if numero % 2 == 0:
        cont_pares += 1
        numeros.insert(0, numero)
    else:
        cont_impares += 1
        numeros.append(numero)
pares = (numeros[0:cont_pares])
impares = (numeros[cont_pares:])
print('=-' * 30)
print(f'Os números digitados são: {numeros}')
print('=-' * 30)
print(f'Os números pares digitados são: {sorted(pares)}')
print(f'Os números impares digitados são: {sorted(impares)}')
print('=-' * 30)