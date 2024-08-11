from datetime import date

dataNasc = [int(input('Digite o ano de nascimento 1: ')),int(input('Digite o ano de nascimento 2: ')),int(input('Digite o ano de nascimento 3: ')),int(input('Digite o ano de nascimento 4: ')),int(input('Digite o ano de nascimento 5: ')),int(input('Digite o ano de nascimento 6: ')),int(input('Digite o ano de nascimento 7: '))]
nMenores = 0
nMaiores = 0
for i in dataNasc:
    idade = date.today().year - i
    if idade < 21:
        nMenores += 1
    else:
        nMaiores += 1

if nMenores == 1:
    print('{} pessoa não atingiu a maior idade.'.format(nMenores))
else:
    print('{} pessoas não atingiram a maior idade.'.format(nMenores))

if nMaiores == 1:
    print('{} pessoa atingiu a maior idade.'.format(nMaiores))
else:
    print('{} pessoas atingiram a maior idade.'.format(nMaiores))