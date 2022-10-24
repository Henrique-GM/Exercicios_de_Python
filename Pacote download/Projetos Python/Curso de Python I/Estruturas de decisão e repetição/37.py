soma = 0

for i in range(1000, 9999 + 1):
    a = str(i)[0]
    b = str(i)[1]
    c = str(i)[2]
    d = str(i)[3]

    ab = a + b
    cd = c + d

    soma += (int(ab) + int(cd))
    soma = soma ** 2

    if str(soma) == str(ab + cd):
        print(soma)

    soma = 0
