valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar?: '))[0].upper()
    if resp in 'N':
        break
valores.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista.')