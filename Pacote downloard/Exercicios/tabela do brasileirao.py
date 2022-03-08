tabela_brasileirao = ('Palmeiras', 'Bragantino', 'Atlético-PR', 'Atlético-MG', 'Fortaleza', 'Bahia', 'Santos',
                      'Atlético-GO', 'Ceará', 'Corinthians', 'Fluminense', 'Flamengo', 'Juventude', 'Internacional',
                      'América-MG', 'São Paulo', 'Sport', 'Cuiabá', 'Chapecoense', 'Grêmio')

print(f'\nOS 5 PRIMEIROS COLOCADOS FORAM\n{tabela_brasileirao[0:5]}')
print(f'\nOS QUATRO PRIMEIROS ÚLTIMOS FORAM\n{tabela_brasileirao[-4:]}')
print(f'\nTIMES EM ORDEM ALFABÉTICA\n{sorted(tabela_brasileirao)}')
print('\nA POSIÇÃO EM QUE SE ENCONTRA:', tabela_brasileirao.index('Chapecoense') + 1)
