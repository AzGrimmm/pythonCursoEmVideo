larguraP = float(input('Qual a largura da parede?: '))
alturaP = float(input('Qual a altura da parede?: '))

área = larguraP * alturaP

tinta = área / 2

litroPorMetro = área / umLitroTintaPinta

print('A parede tem a dimenção {}x{} e sua área é de {}m²'.format(larguraP, alturaP, área))
print('Para pintar toda a parede você precisara de {}l de tinta'.format(tinta))