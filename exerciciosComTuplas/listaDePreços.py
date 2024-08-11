listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 10.00,
            'Estojo', 24.90,
            'Transferidor', 4.80,
            'Compasso', 7.90,
            'Mochila', 119.90,
            'Canetas', 5.97,
            'Livro', 34.90)
print('-' * 38)
print(f'{"LISTAGEM DE PREÇOS":^38}')
print('-' * 38)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-' * 38)