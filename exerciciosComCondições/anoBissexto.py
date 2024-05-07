import datetime

ano = int(input('Digite o ano: '))
if ano == 0:
    ano = datetime.date.today().year
    print('O ano de {} não é bissexto'.format(ano)) 
elif ano % 4 == 0 & ano % 100 != 0:
    print('{} é um ano bisexto!'.format(ano))
elif ano % 4 == 0 & ano % 100 == 0 & ano % 400 == 0:
    print('{} é um ano bisexto!'.format(ano))
else:
    print('{} não é um ano bissexto!'.format(ano))