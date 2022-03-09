import urllib.request

try:
    site = urllib.request.urlopen('https://www.python.org/')

except Exception as erro:
    print(f'O site não está acessível no momento {erro.__class__}')

else:
    print('Tudo Ok')

    # Obtém o código do site
    # print(site.read())
