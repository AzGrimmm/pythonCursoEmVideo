lista = []
solicitar_numero = 'S'
while solicitar_numero[0].upper() in 'S':
    add_numero = int(input('Digite um número: '))
    if add_numero not in lista:
        lista.append(add_numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    solicitar_numero = str(input('Deseja continuar?: '))
    while solicitar_numero[0].upper() not in 'SN':
        solicitar_numero = str(input('Digite um valor valor válido... \nDeseja continuar?: '))
    if solicitar_numero[0].upper() == 'N':
        lista_em_ordem = sorted(lista)
        print(lista_em_ordem)
        break