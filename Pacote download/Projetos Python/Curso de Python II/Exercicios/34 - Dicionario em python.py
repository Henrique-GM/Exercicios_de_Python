aluno = {}

for i in range(0, 1):
    aluno['nome'] = str(input('Digite seu nome: '))
    aluno['media'] = float(input('Digite sua média: '))

    if aluno['media'] >= 7:
        aluno['situacao'] = 'REPROVADO'

    # elif ou if em dicionários
    elif 5 <= aluno['media'] < 7:
        aluno['situacao'] = 'RECUPERAÇÃO'

    else:
        aluno['situacao'] = 'APROVADO'

for chave, valor in aluno.items():
    print(f'{chave} é igual a {valor}')
