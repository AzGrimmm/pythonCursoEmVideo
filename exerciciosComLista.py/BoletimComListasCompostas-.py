ficha = []
while True:
    nome = str(input('Nome: ')).upper()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar?: '))[0].upper()
    while continuar not in 'SN':
        print('Digite um valor válido...')
        continuar = str(input('Quer continuar?: '))[0].upper()
    if continuar == 'N':
        break
print('-=' * 30)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 26)
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
while True:
    opc = int(input('De qual aluno deseja ver as notas/ (-1 interrompe): '))
    if opc <= len(ficha):
        print(f'as notas do aluno(a) {ficha[opc][0]} são: {ficha[opc][1]}' )
    if opc == -1:
        print('Finalizando...')
        break