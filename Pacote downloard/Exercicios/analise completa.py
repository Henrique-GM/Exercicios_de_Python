auxiliar = 0
pessoa_mais_velha = 0
soma = 0
contador = 0
nome_homem = ''

for i in range(1, 4 + 1):

    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite "F" para feminino e "M" para masculino: ')).strip().upper()
    print('\n')

    if auxiliar == 0:
        pessoa_mais_velha = idade
        auxiliar += 1

    elif sexo == 'M' and idade > pessoa_mais_velha:
        pessoa_mais_velha = idade
        nome_homem = nome

    if sexo == 'F' and idade < 20:
        contador += 1

    soma += idade

print('A média da idade do grupo é: {:.2f}'.format(soma / 4))
print('O homem mais velho é: {} com {}'.format(nome_homem, pessoa_mais_velha))
print('A quantidade de mulheres com menos de 20 anos são: {}'.format(contador))