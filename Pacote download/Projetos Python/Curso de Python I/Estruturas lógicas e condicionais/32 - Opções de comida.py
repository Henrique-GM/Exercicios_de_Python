print('\n')
print('OPÇÕES DO CARDÁPIO')
print('\n')
print('COMIDA           CÓDIGO   PREÇO\n'
      'Cachorro quente,  100,     1.20\n'
      'Bauru Simples,    101,     1.30\n'
      'Bauru com ovo,    102,     1.50\n'
      'Hamburguer,       103,     1.20\n'
      'Cheeseburguer,    104,     1.70\n'
      'Suco,             105,     2.20\n'
      'Refrigerante,     106,     1.00')

print('\n')

escolha = int(input('Digite o código da comida: '))
quantidade = int(input('Digite a quantidade que quer: '))

if escolha == 100:
    print(f'O sua escolha desejada é cachorro quente e o total à pagar será {1.20 * quantidade}')

elif escolha == 101:
    print(f'O sua escolha desejada é Bauru Simples e o total à pagar será {1.30 * quantidade}')

elif escolha == 102:
    print(f'O sua escolha desejada é Bauru com ovo e o total à pagar será {1.50 * quantidade}')

elif escolha == 103:
    print(f'O sua escolha desejada é Hamburguer e o total à pagar será {1.20 * quantidade}')

elif escolha == 104:
    print(f'O sua escolha desejada é Cheeseburguer e o total à pagar será {1.70 * quantidade}')

elif escolha == 106:
    print(f'O sua escolha desejada é Suco e o total à pagar será {2.20 * quantidade}')

elif escolha == 107:
    print(f'O sua escolha desejada é Refrigerante e o total à pagar será {1.00 * quantidade}')
