import math

"""

C_O = float(input('Comprimento do cateto oposto: '))
C_A = float(input('Comprimento do cateto adjacente: '))

HI = (C_O ** 2 + C_A ** 2) ** 0.5

print('A hipotenusa vai medir {:.2f}'.format(HI))

"""

C_O = float(input('Comprimento do cateto oposto: '))
C_A = float(input('Comprimento do cateto adjacente: '))

HI = math.hypot(C_O, C_A)

print('A hipotenusa vai medir {:.2f}'.format(HI))