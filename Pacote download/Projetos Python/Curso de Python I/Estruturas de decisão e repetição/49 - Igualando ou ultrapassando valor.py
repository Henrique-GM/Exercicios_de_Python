contador = 1
poupanca_Carlos = 0
poupanca_Joao = 0

salario_Carlos = float(input('Digite o salario de Carlos: '))
salario_Joao = salario_Carlos / 3

for i in range(0, 29):
    poupanca_Carlos += (salario_Carlos * 2 / 100)
    poupanca_Joao += (salario_Joao * 7 / 100)

    print(poupanca_Joao)
    print(poupanca_Carlos)

    if poupanca_Joao >= poupanca_Carlos:
        break

    contador += 1

print(f'Foram necessários {contador} mês(es) para superar a poupança de Carlos')
