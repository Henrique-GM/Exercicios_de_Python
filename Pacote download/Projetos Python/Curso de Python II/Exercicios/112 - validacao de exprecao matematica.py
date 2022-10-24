expressao = str(input('Digite uma expressão: '))

aspasE = expressao.count('(')
aspasD = expressao.count(')')

conta_aspas = aspasE + aspasD

if conta_aspas % 2 == 0:
    print('Expressão correta')

else:
    print('Expressão incorreta')
