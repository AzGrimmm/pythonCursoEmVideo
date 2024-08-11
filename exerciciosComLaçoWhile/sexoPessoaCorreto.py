sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    print('Digite um valor valido!')
    sexo = str(input('Digite o sexo da pessoa: ')).strip().upper()

print('Sexo: {}'.format(sexo))