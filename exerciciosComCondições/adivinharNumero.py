import random

RandomNum = random.randint(0, 5)

adivinhe = int(input('Adivinhe um Número entre 0 e 5: '))
print('O número é {}'.format(RandomNum))

if adivinhe == RandomNum:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! Tente novamente!')