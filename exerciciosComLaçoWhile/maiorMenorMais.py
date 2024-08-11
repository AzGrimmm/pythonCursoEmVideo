mais = str('S')
cont = soma = maior = menor = 0
while mais in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    média = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    mais = str(input('Deseja continuar: ')).strip().upper()[0]
    while mais != 'N' and mais != 'S':
        print('Digite um falor valido!')
        mais = str(input('Deseja continuar: ')).strip().upper()
    if mais == 'N':
        print('Você digitou {} números e a média é {:.2f}'.format(cont, média))
        print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))
        print('Programa finalizado.')