import speedtest

def leitura():
    st = speedtest.Speedtest()
    baixar = st.download()
    subir = st.upload()

    #transformando em GB
    baixarB = baixar / 8 / 1024 / 1000

    #transformando em MB
    baixarb = baixar * (10 ** -6)

    #tranformando em GB
    subirB = subir / 8 / 1024 / 1000

    #tranformando em MB
    subirb = subir * (10 ** -6)

    print('Em GB o download foi em: {:.2f}'.format(baixarB))
    print('Em GB o Upload ficou em: {:.2f}'.format(subirB))
    print('Em MB o download ficou em: {:.2f}'.format(baixarb))
    print('Em MB o Upload foi: {:.2f}'.format(subirb))

if  __name__ == '__main__':
    print('Velocidade da internet (colhendo dados)\n')
    leitura()
