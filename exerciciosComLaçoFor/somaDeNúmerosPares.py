numbers = [int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))]
n = 0
for i in numbers:
    if i % 2 == 0:
        n += i
print(n)