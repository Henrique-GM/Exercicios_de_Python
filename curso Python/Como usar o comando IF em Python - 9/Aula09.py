a = 10
b = 5
res = 0
op = "+"

if op == "+":
    res = a + b

elif op == "-":
    res = a - b

elif op == "*":
    res = a / b

elif op == "/":
    res = a / b

print(str(a) + op + str(b) + " = " + str(res))

c = True

if c:
    print("condicional")

#-------------------------------------------------------
print("\n")

clima = "sol"
dinheiro = 650
lugar = ""

if clima == "sol" or (dinheiro >= 300 and dinheiro <= 500):
    lugar = "clube"

else:
    lugar="cinema"

print("Vou ao " + lugar)
