valores = []
for valor in range(0, 5):
    valores.append(int(input('Digite um número: ')))

print(f'Você digitou os valores: {valores}')
    
menor = maior = valores[valor]

for valor in valores:
    if valor < menor:
        menor = valor

    if valor > maior:
        maior = valor

print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')