#Exercici 17
jugador1 = int(input("Escriu la teua puntuació jugador1: "))
jugador2 = int(input("Escriu la teua puntuació jugador2: "))
jugador3 = int(input("Escriu la teua puntuació jugador3: "))
acumulador1=0
acumulador2=0
acumulador3=0
while True:
    if jugador1<=40:
        acumulador1=int(input("T'orna a escriure la puntuació del jugador1: "))
        jugador1=jugador1 + acumulador1
    if jugador2<=40:
        acumulador2=int(input("T'orna a escriure la puntuació del jugador2: "))
        jugador2= jugador2 + acumulador2
    if jugador3<=40:
        acumulador3=int(input("T'orna a escriure la puntuació del jugador3: "))
        jugador3=jugador3 + acumulador3
    if jugador1>=40:
        print("El guañador és el jugador 1.")
        break
    if jugador2>=40:
        print("El guañador és el jugador 2.")
        break
    if jugador3>=40:
        print("El guañador és el jugador 3.")
        break
    