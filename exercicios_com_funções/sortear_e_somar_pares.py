from random import randint
from time import sleep

def sortear(lista):
    for cont in range(0, 5):
        lista.append(randint(0, 10))
    print(f'Números sorteados foram {lista}.')

def somar_pares(lista):
    soma = 0
    for num in lista: 
        if num % 2 == 0:
            soma += num
    print(f'A soma dos pares na lista: {lista} é: {soma}')
numeros = list()

sortear(numeros)
somar_pares(numeros)
