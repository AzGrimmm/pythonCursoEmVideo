frase = str(input('Digite sua frase: ')).strip()

fraseCount = frase.upper().count('A')
print('A letra A aparece {} vezes na frase.'.format(fraseCount))

FirstTime = frase.upper().find('A') + 1

print('A letra A aparece pela primeira vez na posição {}'.format(FirstTime))

lastTime = frase.upper().rfind('A') + 1

print('A letra A aparece pela ultima vez na posição {}'.format(lastTime))