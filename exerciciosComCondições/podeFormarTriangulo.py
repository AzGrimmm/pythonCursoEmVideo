r1 = int(input('Digite o comprimento da 1ª reta: '))
r2 = int(input('Digite o comprimento da 2ª reta: '))
r3 = int(input('Digite o comprimento da 3ª reta: '))

if r1 + r2 < r3:
    print('Não é possivel formar um triângulo com essas retas!')
elif r1 + r3 < r2:
    print('Não é possivel formar um triângulo com essas retas!')
elif r2 + r3 < r1:
    print('Não é possivel formar um triângulo com essas retas!')
else:
    print('É possivel formar um triângulo com essas retas!')

