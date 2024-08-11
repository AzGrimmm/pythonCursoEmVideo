from random import randint
v = 0
cont = 0
while True:
    jogadaJogador = int(input('Qual sua jogada?: '))
    jogadaMaquina = randint(1, 10)
    total = jogadaJogador + jogadaMaquina
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogadaJogador} e o Computador {jogadaMaquina}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU! vamos jogar novamente...')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo =='I':
        if total % 2 == 1:
            print('Você VENCEU! vamos jogar novamente...')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você venceu {v} vezes.')