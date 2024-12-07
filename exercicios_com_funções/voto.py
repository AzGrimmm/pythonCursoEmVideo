from datetime import datetime

def voto(idade):
    if idade < 16:
        return f'Idade: {idade}, Não vota!'
    elif idade <= 17 or idade > 65:
        return f'Idade: {idade}, Voto opcional!'
    else:
        return f'Idade: {idade}, Voto Obrigatório'


data_atual = datetime.now().year
nascimento = int(input('Ano de nascimento: '))
while nascimento < 1900 or nascimento > data_atual:
    print('Digite um valor válido!')
    nascimento = int(input('Ano de nascimento: '))
idade = data_atual - nascimento

print(voto(idade))