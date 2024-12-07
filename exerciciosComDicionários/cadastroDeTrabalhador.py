from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctpf'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctpf'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - datetime.now().year
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k}: {v}')