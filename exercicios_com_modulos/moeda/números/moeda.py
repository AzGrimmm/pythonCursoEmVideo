def metade(valor = 0):
    res = valor / 2
    return res

def dobro(valor = 0):
    res = valor * 2
    return res

def triplo(valor = 0):
    res = valor * 3
    return res

def aumentar(valor = 0, porcentagem = 0):
    res = valor + (valor * (porcentagem / 100))
    return res

def diminuir(valor = 0, porcentagem = 0):
    res = valor - (valor * (porcentagem / 100))
    return res

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')