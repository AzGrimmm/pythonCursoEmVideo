cont1000 = total = maisbarato = 0
while True:
    preço = 0
    continuar = ' '
    nomeproduto = str(input('Nome do produto: ')).strip().capitalize()
    while preço < 0.20 or preço > 20000:
        preço = float(input('Preço: R$'))
        total += preço
        if preço > 1000:
            cont1000 += 1
        if maisbarato == 0:
            maisbarato = preço
        if preço < maisbarato:
            maisbarato = preço
            nomebarato = nomeproduto
        
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
   
    if continuar == 'N':
        break
 
print(f'O valor total da compra é de: R${total}')
print(f'O número de produtos que custam mais de R$1000,00 é {cont1000}')
print(f'O nome do produto mais barato é {nomebarato}')
print('Programa encerrado.')
