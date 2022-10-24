import uteis

# VANTAGENS

# Organização do código
# Facilidade na manutenção
# Ocultação de código detalhado
# Reutilização em outros projetos

numero = int(input('Digite um valor: '))

fat = uteis.fatotial(numero)

print(f'O fatorial de {numero} é {fat}')
print(f'O dobro de {numero} é {uteis.dobro(numero)}')
