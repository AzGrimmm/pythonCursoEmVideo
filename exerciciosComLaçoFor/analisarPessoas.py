idadeMedia = 0
numeroPessoas = 4
maioridadehomen = 0
totalmulher20 = 0

for pessoa in range(1, numeroPessoas + 1):
    
    print('-' * 5,'{}ª PESSOA'.format(pessoa),'-' * 5) 
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).strip().upper()
    idadeMedia += idade / numeroPessoas
    if pessoa == 1 and sexo in 'M':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totalmulher20 += 1
        
print('A média de idade do grupo é de {:.2f} anos.'.format(idadeMedia))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalmulher20))