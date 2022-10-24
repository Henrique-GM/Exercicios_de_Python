nome = input('Qual é o seu nome: ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = float(input('Digite o primeiro número '))
n2 = float(input('Digite o segundo número '))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoInteira = n1 // n2
esponenciacao = n1**n2
print('A soma vale: {:.3f} o produto {:.3f} e a divisão {:.3f}'.format(soma, multiplicacao, divisao), end=' ')
print('Divisão {:.3f} e potencia {:.3f}'.format(divisao, esponenciacao))

