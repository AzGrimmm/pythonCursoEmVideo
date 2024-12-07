pessoas = []
pessoa = []
pessoas_pesadas = []
pessoas_leves = []
continuar = 'S'
contador = mais_pesado = mais_leve = 0
print('=' * 40)
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mais_leve = mais_pesado = pessoa[1]
    else:
        if mais_leve > pessoa[1]:
              mais_leve = pessoa[1]
        if mais_pesado < pessoa[1]:
             mais_pesado = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar = str(input('Quer continuar?: '))[0].upper()
    
    while continuar not in 'SN':
        print('Digite um valor válido!')
        continuar = str(input('Quer continuar?: '))[0].upper()
    if continuar == 'N':
            break
print('=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'Os dados foram {pessoas}')
print(f'O maior peso foi de {mais_pesado}kg, peso de: ', end='')
for cada_pessoa in pessoas:
     if cada_pessoa[1] == mais_pesado:
          print(f'[{cada_pessoa[0]}]', end='')
print(f'\nO menor peso foi de {mais_leve}kg, peso de: ', end='')
for cada_pessoa in pessoas:
     if cada_pessoa[1] == mais_leve:
          print(f'[{cada_pessoa[0]}]',end='')