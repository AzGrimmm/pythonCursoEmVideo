numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'você digitou os números: {numeros}')

print(f'o número nove apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print(f'O número 3 não apareceu em nenhuma posição.')
for n in numeros:
    if n % 2 == 0:
        print(f'Os números pares são : {n}', end = '')