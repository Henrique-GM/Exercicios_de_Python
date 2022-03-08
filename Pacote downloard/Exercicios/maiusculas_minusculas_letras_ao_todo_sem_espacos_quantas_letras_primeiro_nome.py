nome = str(input('Digite seu nome: '))

print(nome.upper())
print(nome.lower())
print('Numero total de letras:', len(nome) - nome.count(' '))
print('Seu primeiro nome é ' + nome.split()[0] + ' e tem', len(nome.split()[0]), 'letras')
