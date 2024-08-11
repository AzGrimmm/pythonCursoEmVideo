peso =[float(input('Digite o peso 1: ')),float(input('Digite o peso 1: ')),float(input('Digite o peso 1: ')),float(input('Digite o peso 1: ')),float(input('Digite o peso 1: '))]
MenorPeso = peso[0]
MaiorPeso = peso[0]
for i in peso:
    if i < MenorPeso:
        MenorPeso = i
    if i > MaiorPeso  :
        MaiorPeso = i
print(MenorPeso)
print(MaiorPeso)