nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite a quantidade de faltas do aluno: '))
print('\n')

if faltas < 20:
    if nota >= 9.0 and nota <= 10.0:
        print('Seu conceito é A')
    elif nota >= 7.5 and nota <= 8.5:
        print('Seu conceito é B')
    elif nota >= 5.0 and nota <= 7.4:
        print('Seu conceito é C')
    elif nota >= 4.0 and nota <= 4.9:
        print('Seu conceito é D')
    elif nota >= 0.0 and nota <= 3.9:
        print('Seu conceito é E')

elif faltas > 20:
    if nota >= 9.0 and nota <= 10.0:
        print('Seu conceito é B')
    elif nota >= 7.5 and nota <= 8.5:
        print('Seu conceito é C')
    elif nota >= 5.0 and nota <= 7.4:
        print('Seu conceito é D')
    elif nota >= 4.0 and nota <= 4.9:
        print('Seu conceito é E')
    elif nota >= 0.0 and nota <= 3.9:
        print('Seu conceito é E')
