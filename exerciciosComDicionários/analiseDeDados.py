pessoas = []
pessoa = {}

while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['sexo'] = str(input('Sexo: '))[0].upper()
    while pessoa['sexo'] not in 'MF':
        print('ERRO!: Digite um valor válido!')
        pessoa['sexo'] = str(input('Sexo: '))[0].upper()
    pessoa['idade'] = int(input('Idade: '))
    while pessoa['idade'] < 0 or pessoa['idade'] > 100:
        print('ERRO!: Digite um valor valido!')
        pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input('Quer continuar?: '))[0].upper()
    while continuar not in 'SN':
        print('Digite um valor válido!')
        continuar = str(input('Quer continuar?: '))[0].upper()
    if continuar == 'N':
        break
total_pessoas = len(pessoas)
soma = 0
for i, v in enumerate(pessoas):
    soma += v['idade']
    
media_idade = (soma / total_pessoas)
print('-=' * 30)
print(f'Ao todo foram cadastradas: {total_pessoas}')
print('-=' * 30)
print(f'A média de idade é: {media_idade:5.2f}')
print('-=' * 30)
print('As mulheres cadastradas são: ', end='')
for i, v in enumerate(pessoas):
    if v['sexo'] == 'F':
        print(f'{v['nome']}', end=' ')
print('')
print('-=' * 30)
print('As pessoas com idade acima da média são: ')
for i, v in enumerate(pessoas):
    if v['idade'] > media_idade:
        print(f'Nome = {v['nome']}, Idade = {v['idade']}, Sexo = {v['sexo']}')
print('=-' * 30)