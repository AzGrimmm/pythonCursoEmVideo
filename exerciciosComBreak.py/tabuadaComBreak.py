while True:
    n = int(input('Quer ver a tabuada de qual valor?: '))
    if n < 0:
        print('Programa encerrado.')
        break
    for i in range(1,11):
        print(f'{n} x {i} = { n * i}')