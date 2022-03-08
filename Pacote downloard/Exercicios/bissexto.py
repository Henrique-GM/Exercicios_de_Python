from datetime import date

print('Digite 0 para saber o ano e data atual')


ano = int(input('Digite um ano: '))

if ano == 0:
    #ira pergar a data de hoje e o ano
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0:
        print('{} é bissexto'.format(ano))

else:
    print('{} não é bissesto'.format(ano))



