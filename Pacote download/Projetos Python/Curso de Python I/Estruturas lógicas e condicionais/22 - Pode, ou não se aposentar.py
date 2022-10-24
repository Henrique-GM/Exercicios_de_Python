idade = int(input('Digite sua idade: '))
tempo_de_servico = int(input('Digite seu tempo de serviço: '))
print('\n')

if idade >= 65:
    print('Pode aposentar')

elif tempo_de_servico >= 30:
    print('Pode aposentar')

elif idade < 60 and tempo_de_servico >= 25:
    print('pode se aposentar')

else:
    print('Não pode se aposentar')
