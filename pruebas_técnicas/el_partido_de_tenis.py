player1 = 0
player2 = 0
puntuacionplayer1=""
puntuacionplayer2=""
jugador = 0
puntuaciones = []

def pintar(puntuacionplayer1,puntuacionplayer2):
    if puntuacionplayer1 == "Deuce" and puntuacionplayer2 == "Deuce":
        print("Deuce")
    elif puntuacionplayer1 == "Ventaja J1":
        print("Ventaja J1")
    elif puntuacionplayer2 == "Ventaja J2":
        print("Ventaja J2")
    else:
        print(puntuacionplayer1, " - ", puntuacionplayer2)
    

def partido(puntuaciones):
    player1 = 0
    player2 = 0
    for i in puntuaciones:
        try:
            if i not in ["P1","P2"]:
                raise Exception("Error. Las puntuaciones solo pueden ser P1 o P2")
            if i == "P1":
                player1 += 1
            elif i == "P2":
                player2 += 1 
        except ValueError as e:
                print(e)
                continue
        if player1 == 0:
            puntuacionplayer1 = "Love"
        if player1 == 1:
            puntuacionplayer1 = "15"
        if player1 == 2:
            puntuacionplayer1 = "30"
        if player1 == 3 and player2 <= 2:
            puntuacionplayer1 = "40"
        if player1 >=3 and player2 >=3 and player1 == player2:
            puntuacionplayer1 = "Deuce"
            puntuacionplayer2 = "Deuce" 
        if player1 >=4 and player2 >=3 and player1-player2==1:
            puntuacionplayer1 = "Ventaja J1"
            puntuacionplayer2 = ""
        if player1>=4 and player2>=2 and player1-player2==2:
            print("Ha ganado el jugador1")
            break
        if player2 == 0:
            puntuacionplayer2 = "Love"
        if player2 == 1:
            puntuacionplayer2 = "15"
        if player2 == 2:
            puntuacionplayer2 = "30"
        if player2 == 3 and player1 <= 2:
            puntuacionplayer2 = "40"
        if player2 >=3 and player1 >=3 and player1 == player2:
            puntuacionplayer2 = "Deuce"
            puntuacionplayer1 = "Deuce"
        if player2 >=4 and player1 >=3 and player2-player1==1:
            puntuacionplayer2 = "Ventaja J2"
            puntuacionplayer1 = ""
        if player2>=4 and player1>=2 and player2-player1==2:
            print("Ha ganado el jugador2")
            break
        
        pintar(puntuacionplayer1,puntuacionplayer2)
        


