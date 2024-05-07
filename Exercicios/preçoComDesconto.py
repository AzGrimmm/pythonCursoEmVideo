preco = float(input('Qual o preço do produto?: '))

desconto = preco * (5 / 100)

precoComDesconto = preco - desconto

print('O produto de R${:.2f} com desconto de 5%, fica R${:.2f} '.format(preco, precoComDesconto))