valores = []
valor = 0
while valor != 999: 
    valor = int(input('Digite um número: '))
    if valor not in valores and valor != 999:
        valores.append(valor)
ordem_crescente = valores.sort()
print(valores)