termo = int(input('digite o primeiro termo: '))
razão = int(input('digite a razão: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        cont += 1
        print('{} => '.format(termo), end='')
        termo += razão
    print(end=('\n'))      
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Progressão finalizada!')