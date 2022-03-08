from random import randint

aleatorios1 = randint(1, 5)
aleatorios2 = randint(1, 5)
aleatorios3 = randint(1, 5)
aleatorios4 = randint(1, 5)
aleatorios5 = randint(1, 5)

numeros = (aleatorios1, aleatorios2, aleatorios3, aleatorios4, aleatorios5)
print(numeros)

if aleatorios1 >= aleatorios2 and aleatorios1 >= aleatorios3 and aleatorios1 >= aleatorios4 and aleatorios1 >= aleatorios5:
    print(f'O maior foi: {aleatorios1}')

elif aleatorios2 >= aleatorios1 and aleatorios2 >= aleatorios3 and aleatorios2 >= aleatorios4 and aleatorios2 >= aleatorios5:
    print(f'O maior foi: {aleatorios2}')

elif aleatorios3 >= aleatorios1 and aleatorios3 >= aleatorios2 and aleatorios3 >= aleatorios4 and aleatorios3 >= aleatorios5:
    print(f'O maior foi: {aleatorios3}')

elif aleatorios4 >= aleatorios1 and aleatorios4 >= aleatorios2 and aleatorios4 >= aleatorios3 and aleatorios4 >= aleatorios5:
    print(f'O maior foi: {aleatorios4}')

elif aleatorios5 >= aleatorios1 and aleatorios5 >= aleatorios2 and aleatorios5 >= aleatorios3 and aleatorios5 >= aleatorios4:
    print(f'O maior foi: {aleatorios5}')

if aleatorios1 <= aleatorios2 and aleatorios1 <= aleatorios3 and aleatorios1 <= aleatorios4 and aleatorios1 <= aleatorios5:
    print(f'O menor foi: {aleatorios1}')

elif aleatorios2 <= aleatorios1 and aleatorios2 <= aleatorios3 and aleatorios2 <= aleatorios4 and aleatorios2 <= aleatorios5:
    print(f'O menor foi: {aleatorios2}')

elif aleatorios3 <= aleatorios1 and aleatorios3 <= aleatorios2 and aleatorios3 <= aleatorios4 and aleatorios3 <= aleatorios5:
    print(f'O menor foi: {aleatorios3}')

elif aleatorios4 <= aleatorios1 and aleatorios4 <= aleatorios2 and aleatorios4 <= aleatorios3 and aleatorios4 <= aleatorios5:
    print(f'O menor foi: {aleatorios4}')

elif aleatorios5 <= aleatorios1 and aleatorios5 <= aleatorios2 and aleatorios5 <= aleatorios3 and aleatorios5 <= aleatorios4:
    print(f'O menor foi: {aleatorios5}')

# Outra maneira de resolver

numeros = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5),)

print('\n')

print('Os valores sortiados foram: ', end='')

for i in numeros:
    print(f'{i} ', end='')
    # Achando o maior e o menor atravez de uma função(funciona em tuplas)
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')
