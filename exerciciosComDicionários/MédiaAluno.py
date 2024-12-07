ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de: '))
print(ficha.items())
print(f'O aluno {ficha['nome']} tem a média de: {ficha['media']}')

if ficha['media'] <= 5.9:
    print('Reprovado')
else:
    print('Aprovado')