preço = float(input('Valor total?: '))
FormaDePagamento = int(input('Qual a Forma de pagamento?: '))

if FormaDePagamento == 1:
    print('--À vista Dinheiro/Cheque--')
    desconto = preço * 0.10
    preçoComDesconto = preço - desconto
    print('Valor a pagar: R${:.2f}'.format(preçoComDesconto))
elif FormaDePagamento == 2:
    print('--À vista no cartão--')
    desconto = preço * 0.05
    preçoComDesconto = preço - desconto
    print('Valor a pagar: R${:.2f}'.format(preçoComDesconto))
elif FormaDePagamento == 3:
    print('--2x no cartão de credito--')
    parcela = preço / 2
    print('Compra no valor de {:.2f}, será parcelada em 2x de R${:.2f} s/ JUROS.'.format(preço, parcela))

elif FormaDePagamento == 4:
    print('--Parcelado no Cartão de credito--')
    juros = preço * 0.20
    preçoComJuros = preço + juros
    NumParcelas = int(input('Quantas parcelas?: '))
    parcela = preçoComJuros / NumParcelas
    print('Compra no valor de {:.2f}, será parcelada em {}x de R${:.2f} c/ JUROS.'.format(preço, NumParcelas, parcela))
    print('Valor total c/ juros: R${:.2f}'.format(preçoComJuros))
else:
    print('Digite uma forma de pagamento valida!')
    print("""
1--À vista Dinheiro/Cheque--
2--À vista no cartão--
3--2x no cartão de credito--
4--Parcelado no Cartão de credito--   
          """)