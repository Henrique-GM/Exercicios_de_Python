def voto(ano_nascimento):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    if idade < 18:
        return f'você está com {idade} e NÃO VOTA'
    elif idade > 18 and idade < 65:
        return f'você está com {idade} e VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'


ano = int(input('Digite seu ano de nascimento: '))

print(voto(ano))
