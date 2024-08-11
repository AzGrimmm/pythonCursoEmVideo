num = int(input('Digite um número: '))
tot = 0
for c in range(1 , num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        print('{} '.format(c), end=' ')
        tot += 1
    else:
        print('\033[m', end='')
    

if tot == 2:
    print('\n\033[m{} é um número primo.'.format(num))
else:
    print('\n\033[m{} não é um número primo.'.format(num))