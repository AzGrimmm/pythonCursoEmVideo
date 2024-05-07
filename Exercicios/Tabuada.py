n = int(input('Digite um número: '))
print('-' * 12)
for x in range(1, 11):
    m = int(n * x)
    print('{} x {} = {}'.format(n, x, m))

print('-' * 12)