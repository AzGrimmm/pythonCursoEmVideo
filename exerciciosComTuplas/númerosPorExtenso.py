lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
p = -1
while p < 0 or p > len(lista) - 1:
    p = int(input('Digite um numero de 0 a 20: '))
for num in lista:
    if lista.index(num) == p:
        print(f'Você Digitou o número {num}')