matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
soma_pares = soma_coluna3 = maior = 0
for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_coluna3 += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é de: {soma_pares}')
print(f'A soma da 3ª coluna é de: {soma_coluna3}')
print(f'O maior valor da 2ª linha é: {maior}')