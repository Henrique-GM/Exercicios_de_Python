reais_hora = float(input('Digite o quanto recebe por hora: '))
hora_mes = float(input('Digite quantas horas trabalhadas no mês: '))
print('\n')

total_receber = (hora_mes * reais_hora) + (hora_mes * reais_hora * 10 / 100)

print(f'No total você receberá: {total_receber}')
