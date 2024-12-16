
import números.moeda as moeda

p = int(input('Digite o preço: '))
print(f'O preço {moeda.moeda(p)} tem a metade de {moeda.moeda(moeda.metade(p))}')