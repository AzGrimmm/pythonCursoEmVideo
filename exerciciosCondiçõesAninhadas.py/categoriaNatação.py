from datetime import date

anoAtual = date.today().year

anoNasc = int(input('Qual seu ano de nascimento?: '))

idade = anoAtual - anoNasc

if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')
