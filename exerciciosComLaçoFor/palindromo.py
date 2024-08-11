frase = str(input('digite um frase: ')).strip().upper()
print('Você digito a frase {}'.format(frase))
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(junto, inverso)    
if junto == inverso:
    print('A frase é um palindromo!')
else:
    print('A frase não é um palindromo!')