from datetime import date

trabalhador = {}

data_atual = date.today().year

trabalhador['nome'] = str(input('Digite seu nome: '))

ano_nascimento = int(input('Digite o ano que nasceu: '))
trabalhador['idade'] = date.today().year - ano_nascimento

trabalhador['carteira_de_trabalho'] = int(input('Digite sua carteira de trabalho (se não tiver digite 0): '))

if trabalhador['carteira_de_trabalho'] == 0:
    print(trabalhador)

    print(f'\nO indivíduo {trabalhador["nome"]} tem a idade {trabalhador["idade"]} '
          f'e o CTPS com o valor {trabalhador["carteira_de_trabalho"]}')

else:
    trabalhador['ano_contratacao'] = int(input('Digite o ano em que foi contratado: '))
    trabalhador['salario'] = float(input('Digite seu salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['ano_contratacao'] + 35) - data_atual)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
for chave, valor in trabalhador.items():
    print(f'{chave} tem o valor {valor}')
