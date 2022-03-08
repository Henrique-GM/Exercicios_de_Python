# Da quarta posição a seguir
frase = 'Olá Mundo!'
print(frase[4:])

# Se cria uma cópia
print(frase[:])

# Até a quarta posição
frase = 'Olá Mundo!'
print(frase[:4])

# Da primeira posição ao quinto
frase = 'Olá Mundo!'
print(frase[1:5])

# Da primeira posição até o nove pulando uma casas
frase = 'Olá Mundo!'
print(frase[1:9:1])

# Da primera posição, não sabendo o final e pulando uma casa
frase = 'Olá Mundo!'
print(frase[1::1])

# Ate a primeira posição
frase = 'Olá Mundo!'
print(frase[:1])

# Conta quantas vezes um determinado caractere aparece
frase = 'Olá Mundo!'
print(frase.count('o'))

# tranforma os caracteres em maiúsculas
frase = 'Olá Mundo!'
print(frase.upper())

# Conta os caracteres
frase = 'Olá Mundo!'
print(len(frase))

# Troca uma String por outra
frase = 'Olá Mundo!'
print(frase.replace('Mundo', 'Universso'))

# Verifica se existe uma determinada string em uma variável
print('Mundo' in frase)

# Verifica se encontra a primeira posição de uma determinada String
print(frase.find('Olá'))

# Cria uma lista através dos espaços, ou, através de um caractere escolhido
print(frase.split())

# encontrando determinada lista no split
divisor = frase.split()
print(divisor[0])

# encontrando determinada lista no split e seu determinado caractere
print(divisor[1][2])

# primeira palavra em maiúsculo e o resto minúsculo
print(frase.capitalize())

# ele vai transforma os caracteres depois dos espaços em maiúsculos
print(frase.title())

# remove espaços inúteis
print(frase.strip())

# Se a frase estiver em split e junta pelo caractere desejado
'-'.join(frase)
