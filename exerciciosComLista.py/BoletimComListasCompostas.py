ficha = []
while True:
    nome = str(input('nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    print(ficha)
    continuar = str(input('Quer continuar?: '))[0].upper()
    while continuar not in 'SN':
        print('Digite um valor valida!')
        continuar = str(input('Quer continuar?: '))[0].upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"nome":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (-1 interrompe): '))
    if opc == -1:
        print('finalizando...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')