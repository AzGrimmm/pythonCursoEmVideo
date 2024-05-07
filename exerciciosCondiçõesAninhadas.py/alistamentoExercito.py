from datetime import date

anoNasc = int(input('Digite seu ano de nascimento: '))

anoAtual = date.today().year

idade = anoAtual - anoNasc

if idade < 18:
    a = 18 - idade
    if a == 1:
        print('falta apenas {} ano para seu alistamento.'.format(a))
    else:
        print('Faltam {} anos para para seu alistamento.'.format(a))
elif idade == 18:
    print('Esta na hora de se alistar no serviço militar')
else:
    print('Passou do tempo de se alistar no serviço militar.')