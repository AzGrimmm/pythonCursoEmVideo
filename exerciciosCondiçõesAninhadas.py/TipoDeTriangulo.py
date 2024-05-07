r1 = int(input('Digite o comprimento da 1ª reta: '))
r2 = int(input('Digite o comprimento da 2ª reta: '))
r3 = int(input('Digite o comprimento da 3ª reta: '))

if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:
    print('Não é possivel formar um triângulo com essas retas!')
else:
    print('As retas acima podem formar um triâgulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')


    