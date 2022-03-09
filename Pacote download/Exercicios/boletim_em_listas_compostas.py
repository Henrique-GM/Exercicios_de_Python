informacoes_alunos = []
boletim = []
media = 0

while True:
    informacoes_alunos.append(str(input('\nDigite seu nome: ')))
    informacoes_alunos.append(float(input('Digite sua primeira nota: ')))
    informacoes_alunos.append(float(input('Digite sua segunda nota: ')))

    # Uma outra forma de inserir na lista boletim.append([nome], [nota1, nota2], media)

    boletim.append(informacoes_alunos[:])
    informacoes_alunos.clear()

    escolha = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    if escolha != 'S':
        break

print('\n')

for i, valor in enumerate(boletim):
    media = (valor[1] + valor[2]) / 2

    print(f'{valor[0]} de número {i} obteve a média: {media}')

print('\n')

while True:
    escolha_mostrar = int(input('\nDigite o número do respectivo aluno(digite 999 pra parar): '))

    if escolha_mostrar == 999:
        break

    mostrar = boletim[escolha_mostrar]

    print(f'As notas de {mostrar[0]} foram {mostrar[1], mostrar[2]}')
