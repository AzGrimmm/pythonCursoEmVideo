def fatorial(num=1, show=False):
    f = 1
    
    for c in range(num, 0, -1):
        f *= c
        print(c, end='x')

fatorial(5)