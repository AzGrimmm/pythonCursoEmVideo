c = 0
n = 0

for i in range(1, 501, 2):
        if i % 3 == 0:
            c += 1
            n += i
print('Foram somados {} números'.format(c))   
print('A soma dos números é igual a {}'.format(n))