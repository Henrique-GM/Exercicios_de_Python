def aumentar(valor, moeda=False):
    adiciona = valor * 10 / 100
    valor += adiciona

    if moeda:
        return f'R${valor:.2f}'.replace('.', ',')

    return valor


def dobro(valor, moeda=False):
    valor *= 2

    if moeda:
        return f'R${valor:.2f}'.replace('.', ',')

    return valor


def reduzir(valor, moeda=False):
    diminui = valor * 13 / 100
    valor -= diminui

    if moeda:
        return f'R${valor:.2f}'.replace('.', ',')

    return valor


def metade(valor, moeda=False):
    valor /= 2

    if moeda:
        return f'R${valor:.2f}'.replace('.', ',')

    return valor


def precoAnalisado(valor, moeda=False):
    if moeda:
        return f'{valor:.2f}'.replace('.', ',')

    return valor


def resumo(valor, aumento, reducao):
    print(f'Preço analisado:\t\tR${precoAnalisado(valor, True)}')

    print(f'O dobro do valor é:\t\t{dobro(valor, True)}')

    print(f'A metade do valor foi:\t{metade(valor, True)}')

    print(f'{reducao}% de redução:\t\t\t{reduzir(valor, True)}')

    print(f'{aumento}% de aumento:\t\t\t{aumentar(valor, True)}')
