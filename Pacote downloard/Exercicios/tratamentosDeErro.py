try:
    a = int(input('Digite um número: '))
    b = int(input('Digite outro número: '))
    r = a / b

# exceção genérico
# except Exception as erro:
# print(f'O problema encontrado foi: {erro.__class__}')

except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero')

else:
    print(f'O resultado é {r:.2f}')

finally:
    print('Obrigado(a)! volte sempre')
