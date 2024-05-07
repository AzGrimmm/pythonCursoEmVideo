from random import randint

maquina = randint(1, 3)

if maquina == 1:
    maquina = 'Pedra'
elif maquina == 2:
    maquina = 'Papel'
else:
    maquina = 'Tesoura'

maquina = maquina.upper()
jogador = str(input('Pedra, papel ou tesoura?: ')).upper()
print('-=' * 10)
print('Maquina: {}'.format(maquina))
if jogador != 'PEDRA' and jogador != 'PAPEL' and jogador != 'TESOURA':
    print('-=' * 10)
    print('Digite um valor valido!')
elif jogador == maquina:
    print('Jogador: {}'.format(jogador))
    print('-=' * 10)
    print('Empate')
elif jogador == 'PEDRA' and maquina == 'PAPEL' or jogador == 'PAPEL' and maquina == 'TESOURA' or jogador == 'TESOURA' and maquina == 'PEDRA':
    print('Jogador: {}'.format(jogador))
    print('-=' * 10)
    print('Maquina: GANHEIII!')
else:
    print('Jogador: {}'.format(jogador))
    print('-=' * 10)
    print('Maquina: Você GANHOU!')