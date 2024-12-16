def notas(*notas, sit=False):
    """

    => Analiza várias notas e mostra o total de notas, a maior nota, 
    a menor nota, a média e a situação.
    :param 1: varias notas.
    :param 2: sit = (True ou False), se for True, mostra a situação
    :return: um dicionário com todos os dados.    
    """    
    maior = menor = soma = 0
    
    for x in notas:
        if x > maior:
            maior = x
        if x < menor or menor == 0:
            menor = x
        soma += x
    media = soma / len(notas)

    dicionario = {'total':len(notas), 'maior': maior, 'menor':menor, 'média': media}

    if sit == True:
        if media < 6:
            dicionario['situação'] = 'Ruim'
        elif media < 7:
            dicionario['situação'] = 'Razoavel'
        elif media < 9:
            dicionario['situação'] = 'Boa'
        else:
            dicionario['situação'] = 'Ótima'

    return dicionario

ficha = notas(10,10,10, sit=True)
print(ficha)
help(notas)