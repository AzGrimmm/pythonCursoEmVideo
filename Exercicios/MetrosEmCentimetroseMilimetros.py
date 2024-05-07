metros = int(input('Digite o valor em metros: '))

quilômetro = metros / 1000

hectômetro = metros / 100

decâmetro = metros / 10

decímetro = metros * 10

centimetros = metros * 100

milimetros = metros * 1000

print('{} metros são: {}mn, {}cm, {}dm, {}dam, {}hm, {}km '.format(metros, milimetros, centimetros, decímetro, decâmetro, hectômetro, quilômetro))
