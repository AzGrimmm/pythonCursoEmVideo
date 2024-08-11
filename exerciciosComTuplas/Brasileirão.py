times = ('Flamengo', 'Bahia', 'Botafogo', 'CA Paranaense', 'São Paulo FC', 'Palmeiras', 'Cruzeiro', 'Atletico Mineiro', 'Red Bull Bragantino', 'Internacional', 'Fortaleza', 'EC Juventude', 'Gremio', 'Vasco Gama', 'Corinthians', 'Fluminense', 'Criciúma', 'AC Goianiense', 'Cuiabá Esporte Clube', 'EC Vitória')
cincoprimeiros = times[:5]
cincoultimos = times[15:]
alfabetica = sorted(times)

print('=-' * 40)

print('Times em suas determinadas posições:')
print(times)
print('=-' * 40)
print('Os cinco primeiros colocados são:')
print(cincoprimeiros)
print('=-' * 40)
print('Os ultimos colocados são:')
print(cincoultimos)
print('=-' * 40)
print('Os times em ordem alfabética:')
print(alfabetica)
print('=-' * 40)
for i in times:
    if i == 'Palmeiras':
        print(f'A colocação do palmeiras é a: {times.index(i) + 1}ª')
print('=-' * 40)