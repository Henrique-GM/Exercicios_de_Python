idade_nadador = int(input('Digite a idade do nadador: '))
print('\n')

if idade_nadador >= 5 and idade_nadador <= 7:
    print('infantil A')

elif idade_nadador >= 8 and idade_nadador <= 10:
    print('infantil B')

elif idade_nadador >= 11 and idade_nadador <= 13:
    print('juvenil A')

elif idade_nadador >= 14 and idade_nadador <= 17:
    print('juvenil B')

elif idade_nadador >= 18:
    print('Sênior')
