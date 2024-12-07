from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
jogador = {}
ranking = []

for i in range(0,4):
    jogo[f'jogador{i + 1}'] = randint(1, 6)

for k, v in jogo.items():
    print(f'{f'O jogador {k} tirou {v}':^30}')
    sleep(1)
print(f'Ranking de jogadores:')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{f'{i + 1}º lugar: {v[0]} com {v[1]}.':^30}')
    sleep(1)
