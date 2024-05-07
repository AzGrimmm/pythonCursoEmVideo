valorCasa = float(input('Qual o valor da casa?: '))
renda = float(input('Qual sua renda mensal?: '))
anosPagando = int(input('Em quantos anos vai pagar?: '))

meses = anosPagando * 12
valorPrestacao = valorCasa / meses
renda30pc = renda * 0.30

if valorPrestacao > renda30pc:
    print('Seu empréstimo foi negado, pois a parcela mensal ultrapassa os 30% de sua renda.')
else:
    print('Seu empréstimo foi aprovado!')

