def metade(valor=0, format=False):
    res = valor / 2
    return res if format is False else moeda(res)


def dobro(valor=0, format=False):
    res = valor * 2
    return res if format is False else moeda(res)


def triplo(valor=0, format=False):
    res = valor * 3
    return res if format is False else moeda(res)


def aumentar(valor=0, porcentagem=0, format=False):
    res = valor + (valor * (porcentagem / 100))
    return res if format is False else moeda(res)


def diminuir(valor=0, porcentagem=0, format=False):
    res = valor - (valor * (porcentagem / 100))
    return res if format is False else moeda(res)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor=0, aumento=0, reducao=0):
    print('-' * 33)
    print('RESUMO DO VALOR'.center(33))
    print('-' * 33)
    print(f'Preço analizado: \t{moeda(valor)}')
    print(f'Dobro: \t\t\t{dobro(valor, True)}')
    print(f'Metade: \t\t{metade(valor, True)}')
    if aumento != 0:
        print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    if reducao != 0:
        print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print('-' * 33)
