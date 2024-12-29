def text(txt):
    print('-' * 30)
    print(f'{txt}'.center(30))
    print('-' * 30)


def options():
    text = """
 1 - Ver pessoas cadastradas.
 2 - Cadastrar um pessoa.
 3 - Fechar menu.
"""
    print(f'{text:<30}')
    print('-' * 30)


def leiaOption(msg):
    while True:
        try:
            num = int(input(msg))
            if num < 1 or num > 3:
                print('ERRO! Digite uma opção válida!')
                continue
        except (ValueError, TypeError):
            print('ERRO! Digite uma Opcão válida')
        else:
            return num


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Digite um número inteiro válido!')
            continue
        else:
            return num
