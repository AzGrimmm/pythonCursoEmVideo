from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
tot = 1
print('-' * 51)
print(f'{'JOGA NA MEGA SENA':^51}')
print('-' * 51)
quant = int(input('Quantos jogos você quer que eu sorteie?: '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=' * 8, f'{f'SORTEANDO {quant} JOGOS':^9}', '=-' * 8)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*8, f'{f'< BOA SORTE! >':^17}', '=-' * 8)