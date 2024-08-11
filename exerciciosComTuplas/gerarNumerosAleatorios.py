from random import randint

numeros = (randint(0, 101), randint(0, 101), randint(0, 101), randint(0, 101), randint(0, 101))
menor = numeros[0]
maior = numeros[0]
print(f'Os números sorteados são: ', end = '')
for n in numeros:
    print(f'{n} ', end = '')
print(f'\nO menor número é {max(numeros)}')
print(f'O maior número é {min(numeros)}')