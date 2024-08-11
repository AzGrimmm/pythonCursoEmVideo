from time import sleep

opção = 6

while opção == 6:
    for numbers in range(0, 2):
        num = float(input('Digite um número: '))
        if numbers == 0:
            n1 = num
        else:
            n2 = num
    opção = 8
    while opção == 8:
        sleep(0.5)
        print('''--DIGITE:--
        [1] PARA SOMAR
        [2] PARA SUBTRAIR
        [3] PARA MULTIPLICAR
        [4] PARA DIVIDIR
        [5] PARA MOSTRAR QUAL O MAIOR
        [6] PARA NOVOS NÚMEROS
        [7] PARA SAIR DO PROGRAMA''')

        opção = int(input('Opção: '))

        while opção < 1 or opção > 8:
            print('Digite uma opcão valida.')
            opção = int(input('Opção: '))

        if opção == 1:
            soma = n1 + n2
            print(soma)
            opção = 8

        elif opção == 2:
            subtração = float(n1 - n2)
            print(subtração)
            opção = 8

        elif opção == 3:
            multiplicação = n1 * n2
            print(multiplicação)
            opção = 8
        elif opção == 4:
            divisão = n1 / n2
            print(divisão)
            opção = 8

        elif opção == 5:
            if n1 == n2:
                print('Os dois números são iguais.')
            else:
                maior = 0
                if n1 > n2:
                    print('O maior número é: {}'.format(n1))
                else:
                    print('O maior número é: {}'.format(n2))
            opção = 8

        elif opção == 7:
            w = str(input('Digite R para reiniciar ou F para encerrar o programa[R/F]: ')).strip().upper()
            while w != 'R' and w != 'F':
                print('digite uma opção valida.')
                w = str(input('[R] para reiniciar ou [F] para encerrar[R/F]: ')).strip().upper()
            if w =='R':
                opção = 6
            elif w == 'F':
                print('Finalizando...')
                sleep(1)
                print('Finalizado.')
                break