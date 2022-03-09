from datetime import date

idade = int(input('Digite o ano de seu nascimento: '))

comparar = date.today().year -idade

if comparar >= 9 and comparar <= 14:
    print('MIRIM')

elif comparar >= 14 and comparar <= 19:
    print('INFANTIL')

elif comparar >= 19 and comparar <= 20:
    print('JUNIOR')

elif comparar <= 25:
    print('SÊNIOR')

elif comparar > 25:
    print('MASTER')