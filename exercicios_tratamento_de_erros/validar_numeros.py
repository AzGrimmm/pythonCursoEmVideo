def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('Erro! o programa foi interrompido pelo usuário.')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número real válido.')
        else:
            return num


int = leiaInt('Digite um número inteiro: ')
print(f'Você digitou {int} e é um número inteiro')
float = leiaFloat('Digite um número real: ')
print(f'Você digitou {float} e é um número real')