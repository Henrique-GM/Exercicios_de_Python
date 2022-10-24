fib1 = 0
fib2 = 1
fib3 = 0

numero = int(input('Digite um número: '))

for fibonacci in range(0, numero):

    if fibonacci == 0:
        print(0)

    elif fibonacci == 1:
        print(1)

    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3

    print(fib3)
