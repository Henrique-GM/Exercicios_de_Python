valores = []
for i in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {i}: ')))

print(f'\nO maior valor é {max(valores)} na posição ', end='')

for index, valor in enumerate(valores):
    if valor == max(valores):
        print(f'...{index}', end='')

print(f'\nO menor valor é {min(valores)} na posição ', end='')

for index, valor in enumerate(valores):
    if valor == min(valores):
        print(f'...{index}', end='')
