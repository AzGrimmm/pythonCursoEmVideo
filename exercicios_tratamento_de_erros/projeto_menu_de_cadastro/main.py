from func import arquivo
from func import sistema
from time import sleep

arq = 'exercicios_tratamento_de_erros/projeto_menu_de_cadastro/pessoas_cadastradas.txt'

if not arquivo.arquivoExiste(arq):
    print('Arquivo não encontrado')
    arquivo.criarArquivo(arq)

option = 0

while True:
    sistema.text('MENU PRINCIPAL')
    sistema.options()
    option = sistema.leiaOption('option: ')
    if option == 3:
        print('Finalizando...')
        sleep(1)
        break
    elif option == 2:
        sistema.text('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = sistema.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif option == 1:
        sistema.text('Opção 1')
        arquivo.lerArquivo(arq)
