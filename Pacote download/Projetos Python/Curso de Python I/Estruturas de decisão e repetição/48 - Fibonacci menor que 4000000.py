fib1 = 0
fib2 = 1
fib3 = 0

numero = int(input('Digite um número: '))

for i in range(0, numero):

    if i == 0:
        print(0)

    elif i == 1:
        print(1)

    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3

    if fib3 < 4000000:
        print(fib3)

    else:
        break
