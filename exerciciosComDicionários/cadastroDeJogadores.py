dados = {}
dados['nome'] = str(input('Qual o nome do jogador?: '))
dados['gols'] = []
dados['total_gols'] = 0
total_partidas = int(input(f'Quantas partidas {dados['nome']} jogou?: '))
for i in range(0, total_partidas):
    dados['gols'].append(int(input(f'Quantos gols na partida {i+1}: ')))
    dados['total_gols'] += dados['gols'][i]
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'    O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados['nome']} jogou {total_partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i + 1}, fez {v} gols.')
print(f'foi um total de {dados["total_gols"]} gols.')