jogadores = []
dados = {}
continuar = 'S'
while continuar == 'S':
    dados['nome'] = str(input('Qual o nome do jogador?: '))
    dados['gols'] = []
    dados['total_gols'] = 0
    total_partidas = int(input(f'Quantas partidas {dados['nome']} jogou?: '))
    for i in range(0, total_partidas):
        dados['gols'].append(int(input(f'Quantos gols na partida {i+1}: ')))
        dados['total_gols'] += dados['gols'][i]
    jogadores.append(dados.copy())
    dados.clear()
    continuar = str(input('Quer continuar?: '))[0].upper()
print('=-' * 30)
print(f'{'cod':<4}{'nome':<15}{'gols':<15}{'total':<5}')
print('-' * 50)
for i, v in enumerate(jogadores):
    print(f'{i:<4}{v['nome']:<15}{v['gols']}{v['total_gols']:>14}')
print('=-' * 30)
escolha = -2
while escolha != -1:
    escolha = int(input('Mostrar dados de qual jogador? (-1 para parar): '))
    try: 
        for i, v in enumerate(jogadores):
            if escolha == i:
                print(f' -- LEVANTAMENTO DO JOGADOR {v['nome']}:')
                for f, ngols in enumerate(v['gols']):
                    print(f'    No jogo {f + 1} fez {ngols}.')
    except IndexError:
        print('Digite um valor valido!')
        escolha = int(input('Mostrar dados de qual jogador? (-1 para parar): '))
print('Fechando programa...')