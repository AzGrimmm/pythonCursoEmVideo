num = int(input('Digite um número: '))

for i in range(1, 11):
    res = num * i
    print('{} x {} = {}'.format(num, i, res))