n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('{} é o maior e {} é o menor!'.format(n1 ,n2))
elif n2 > n1:
    print('{} é o maior e {} é o menor!'.format(n2, n1))
else:
    print('Os dois números são iguais!')