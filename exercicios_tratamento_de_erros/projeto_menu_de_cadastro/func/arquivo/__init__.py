from func import sistema


def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except ():
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Aruivo {arquivo} criado com sucesso.')


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except ():
        print('Houve um erro ao abrir o arquivo')
    else:
        sistema.text('Pessoas cadastradas...')
        for linha in a:
            dado = linha.split(';')
            try:
                dado[1] = dado[1].replace('\n', '')
            except (IndexError):
                print('não existe nenhum cadastro!')
            else:
                print(f'{dado[0]:<20}{dado[1]:>3} anos.')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except ():
        print('Erro ao tentar ler o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except ():
            print('Erro ao tentar efetuar o cadastro!')
        else:
            print('cadastro efetuado com sucesso!')
        a.close()
