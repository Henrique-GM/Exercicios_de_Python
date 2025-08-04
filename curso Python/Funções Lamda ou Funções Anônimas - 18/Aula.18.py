# São funções simples e anônimas, não precisa por none da função. Vai retornar um valor sem o return.

soma = lambda a, b: a + b
print(soma(2, 5))

multiplicacao = lambda a, b, c: (a + b * c)
print(multiplicacao(2, 3, 5))

r = lambda x, func: x + func(x) # Passando uma fução lambda, dentro de outra.
resposta = r(2, lambda x: x * x)
print(resposta)