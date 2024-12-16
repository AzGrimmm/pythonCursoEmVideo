def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols.')

def is_number(string):
    try:
        int(string)
        return True
    except:
        return False


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')

while is_number(gols) == False:
    if is_number(gols):
        gols = int(gols)
    else:
        gols = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
