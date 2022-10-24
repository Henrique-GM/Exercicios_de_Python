
variavel = input('Digite algo: ')
print('Essa variavel é: ', type(variavel))

# Se for número o isnumeric vai retornar um true
print('Ele é um numero? ', variavel.isnumeric())

# Se for alfabeto o isalpha vai retornar um true
print('Ele é um alfabeto? ', variavel.isalpha())

# Se for alfanumerico o isalnum vai retornar um true
print('Ele é alfanumérico? ', variavel.isalnum())

# Vê se a string digitada está em letras maiusculas retorna true
print('Está em maiúsculo? ', variavel.isupper())

# se for ascii retorna true
print('Está em ascii? ', variavel.isascii())

# Se for decimal retorna true
print('É decimal? ', variavel.isdecimal())

# Se for um digito retorna true
print('É um dígito? ', variavel.isdigit())

# Se for um identificador retorna true
print('É um identificador? ', variavel.isidentifier())

# Se for um string minusculo retorna true
print('Éstá em minusculo? ', variavel.islower())

# Se for imprimivel retorna true
print('É imprimivel? ', variavel.isprintable())

# Se for um espaço retorna true
print('É um espaço? ', variavel.isspace())

# Se for captalizada(quando tem letrar maiuscula e minusculas) retorna true
print('É um titulo? ', variavel.istitle())