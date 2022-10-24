nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

if nota1 > 0 and nota1 < 10:
    if nota2 > 0 and nota2 < 10:
        print(f'O valor da média é {(nota1 + nota2) / 2:.2f}')
else:
    print('Notas invalidas')
