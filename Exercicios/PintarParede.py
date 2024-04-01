larguraP = int(input('Quantos metros de largura tem a parede?: '))
alturaP = int(input('Quantos metros de altura tem a parede?: '))

area = larguraP * alturaP

litroTintaPorMetro = 2**2

litroPorMetro = area / litroTintaPorMetro

print('A parede tem {} metros quadrados, você usara {} litros de tinta para pintura total'.format(area, litroPorMetro))
