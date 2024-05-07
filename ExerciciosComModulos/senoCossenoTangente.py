import math

ângulo = float(input('digite o ângulo que deseja: '))

seno = math.sin(math.radians(ângulo))
cossêno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))

print('O ângulo de {} tem o SENO de {:.2f}, COSSÊNO de {:.2f} e TANGENTE de {:.2f}'.format(ângulo, seno, cossêno, tangente))