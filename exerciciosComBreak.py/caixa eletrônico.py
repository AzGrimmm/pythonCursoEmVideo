valor = saque = cont50 = cont20 = cont10 = cont1 = 0

while valor < 1 or valor > 20000:
    valor = int(input('Qual valor quer sacar: R$'))
    if valor > 20000:
        print('Você pode sacar até R$20.000,00')
    while saque + 50 <= valor:
        cont50 += 1
        saque += 50
    while saque + 20 <= valor:
        cont20 += 1
        saque += 20
    while saque + 10 <= valor:
        cont10 += 1
        saque += 10
    while saque + 1 <= valor:
        cont1 += 1
        saque += 1
print('=' * 40)
print(f'Total de cédulas de R$50 = {cont50}')
print(f'Total de cédulas de R$20 = {cont20}')
print(f'Total de cédulas de R$10 = {cont10}')
print(f'Total de cédulas de R$1 = {cont1}')
print('=' * 40)
print('Volte Sempre! Bom dia!')
        