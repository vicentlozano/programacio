import random

def treuCarta():
    valors = "123456789XJQK"
    pals = "CDPT"
    valAleatori = random.randrange (0,12)
    palAleatori = random.randrange (0,3)
    return valors[valAleatori] + pals[palAleatori]

def valorMa(ma):
    valorMa=0
    arrMa = ma.split("#")
    for i in arrMa:
        if i != '':
            if i[0] in "XJQK":
                valor = 10
            else:
                valor = int(i[0])
            valorMa = valorMa + valor
    return valorMa

valorPlantaBanca = 10
valorMaBanca = 0
valorMaJugador = 0

maBanca = ""
maJugador = ""
seguir = True
nova_partida = True
acum_punts_jugador = 0
num_partides = 0
while nova_partida:
    num_partides = num_partides + 1

    while valorMaBanca < valorPlantaBanca:
        carta = treuCarta()
        while carta in maBanca or carta in maJugador:
            carta = treuCarta()
        maBanca = maBanca + carta + "#"
        valorMaBanca = valorMa(maBanca)


    while valorMaJugador < 21 and seguir:
        carta = treuCarta()
        while carta in maBanca or carta in maJugador:
            carta = treuCarta()
        maJugador = maJugador + carta + "#"
        valorMaJugador = valorMa(maJugador)
        print (maJugador + " valor: " + str(valorMaJugador))
        if valorMaJugador > 21:
            print ("T'has passat")
            break
        elif valorMaJugador == 21:
            print ("BlackJack!!!")
            break
        print ("Vols altra carta (S/N)?")
        resposta= input()
        if (resposta.upper()=='N'):
            seguir = False

    print ("Banca: " + maBanca + " valor: " + str(valorMaBanca))
    print ("Vols jugar un altra partida (S/N)?")
    resposta= input()
    if (resposta.upper()=='N'):
        nova_partida = False
    if (resposta.upper()=='S'):
        if valorMaJugador > 21:
            valorMaJugador = 22
        acum_punts_jugador = acum_punts_jugador + valorMaJugador
        valorPlantaBanca =(int)(acum_punts_jugador / num_partides)
        valorMaBanca = 0
        valorMaJugador = 0
        maBanca = ""
        maJugador = ""
        seguir = True      