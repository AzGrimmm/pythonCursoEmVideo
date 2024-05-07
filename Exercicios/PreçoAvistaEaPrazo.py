Preço = float(input('Qual o preço do produto?'))
desconto = Preço * (5 / 100)
juros = Preço * (8 / 100)
PreçoaVista = Preço - desconto
PreçoaPrazo = Preço + juros

print('O preço do produto é R${}, a vista é R${} e a Prazo é R${}'.format(Preço,PreçoaVista,PreçoaPrazo))
print