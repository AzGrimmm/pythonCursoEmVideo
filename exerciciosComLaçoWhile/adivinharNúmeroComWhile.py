from random import randint

NumRandom = randint(0, 10)
NumPalpites = 0

adivinhe = int(input('Pense em um número de 0 a 5: '))
while adivinhe < 0 or adivinhe > 5:
    print('Valor errado.')
    adivinhe = int(input('Pense em um número de 0 a 5: '))
while adivinhe != NumRandom:
    print('Você Errou!')
    adivinhe = int(input('Pense em um número de 0 a 5: '))
    NumPalpites += 1

print('Você acertou!')
print('Foram necessários {} palpites para vencer.'.format(NumPalpites + 1))