from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento: '))
data_atual = date.today().year

if data_atual - ano_nascimento < 18:
    print('Ainda vai se alistar no exercito')
    print('Você tem {} anos. Precisa ter 18'.format(data_atual - ano_nascimento))

elif data_atual - ano_nascimento > 18:
    print('Voçê tem {} anos. Passou a idade mínima de 18 para se alistar'.format(data_atual - ano_nascimento))

else:
    print('Está na hora do alistamento')