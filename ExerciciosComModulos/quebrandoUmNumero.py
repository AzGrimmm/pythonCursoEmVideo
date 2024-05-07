from math import trunc

num = float(input('Digite um número: '))

numInt = trunc(num)

print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, numInt))