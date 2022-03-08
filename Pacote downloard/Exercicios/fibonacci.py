f1 = 0
f2 = 1
fn = 0

numero = int(input('Digite um número inteiro: '))

i = 1
while i <= numero:

 if i == 1:
  print(f1)
 elif i == 2:
  print(f2)

 fn = f1 + f2
 f1 = f2
 f2 = fn

 print(fn)

 i = i + 1