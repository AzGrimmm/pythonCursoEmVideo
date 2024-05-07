a = int(input('Digite um número: ')) 
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))

# verificando quem é o menor.
menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
    
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('{} é o menor número!'.format(menor))
print('{} é o maior número!'.format(maior))

