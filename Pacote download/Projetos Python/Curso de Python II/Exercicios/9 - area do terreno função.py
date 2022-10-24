def area(largura, altura):
    resultado = largura * altura
    print(f'A área de um terreno {largura}x{altura} é de {resultado:.2f}m²')


largura = float(input('Digite a largura: '))
altura = float(input('Digite a largura: '))

print()

area(largura, altura)
