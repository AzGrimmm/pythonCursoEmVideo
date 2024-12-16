def voto(ano):
    from datetime import datetime
    data_atual = datetime.now().year
    idade = data_atual - ano
    if idade < 16:
        return f'Idade: {idade}, Não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Idade: {idade}, Voto opcional!'
    else:
        return f'Idade: {idade}, Voto Obrigatório'

    
nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))