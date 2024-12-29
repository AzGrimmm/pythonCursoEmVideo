
from utilidades import moeda
from utilidades import dados

p = dados.leia_dinheiro('Digite o preço: ')

moeda.resumo(p, 15, 80)
