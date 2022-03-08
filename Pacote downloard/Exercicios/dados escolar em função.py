def notas(*numeros, sit=False):
    # para retornar um dicionário em uma função tem que ser dict()
    d = dict()
    d['total'] = len(numeros)
    d['maior'] = max(numeros)
    d['menor'] = min(numeros)
    d['media'] = sum(numeros) / len(numeros)

    if sit:
        if d['media'] >= 7:
            d['situacao'] = 'BOA'

        elif d['media'] >= 5:
            d['situacao'] = 'RAZOÁVEL'

        else:
            d['situacao'] = 'RUIM'

    return d


print(notas(1, 2, 3, 4, 6, sit=True))
