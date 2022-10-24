soma1 = 0
soma2 = 0
for i in range(1, 100 + 1):
    soma1 += i ** 2
    
print(f'A soma dos quadrados foi: {soma1}')

for z in range(1, 100 + 1):
    soma2 += z

print(f'O quadrado da soma foi: {soma2 ** 2}')
print(f'A diferença entre eles é: {soma1 - soma2}')
