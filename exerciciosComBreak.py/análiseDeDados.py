while True:
    cont = homens = mulheresate20 = 0
    idade = -1
    sexo = ' '
    continuar = ' '

    while idade < 1 or idade > 110:
        idade = int(input('Idade: '))
        if idade < 1 or idade > 110:
            print('Digite um valor válido.')

    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if sexo not in 'MF':
            print('Digite um valor válido.')
    if sexo == 'M':
        homens += 1
    if idade > 17:
        cont += 1
    if sexo == 'F' and idade <= 20:
        mulheresate20 += 1

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        print(f'Total de pessoas com 18 anos ou mais é de : {cont}')
        print(f'Total de homens cadastrados é de: {homens}')
        print(f'Total de mulheres com 20 anos ou menos é de: {mulheresate20}')
        print('Programa encerrado')
        break