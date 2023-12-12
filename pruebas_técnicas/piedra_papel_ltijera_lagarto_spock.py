def juego (jugadas):
#! Defiinmos las reglss del juego:
    #! 1. Piedra gana a tijeras y lagarto
    #! 2. Papel gana a piedra y spock
    #! 3. Tijeras gana a papel y lagarto
    #! 4. Lagarto gana a papel y spock
    #! 5. Spock gana a piedra y tijeras
    #! 6. Empate si ambos sacan lo mismo
    reglas = {"piedra": ["tijeras","lagarto"], "papel": ["piedra","spock"],
            "tijeras": ["papel","lagarto"], "lagarto": ["papel","spock"],
            "spock": ["piedra","tijeras"]}
    player1 = 0
    player2 = 0
    for i,j in jugadas:
        if i == j:
            None
        elif j in reglas[i]:
            player1 +=1
        elif i in reglas[j]:
            player2 +=1
    #! Recordar que si no hay return, la función devuelve None
    #! Además, tenemos que acordarnos que podemos poner un if en una sola linea, asi queda más profesional
    return "empate" if player1==player2 else "Ha ganado el Player1" if player1>player2 else "Ha ganado el Player"
    #*pruebas:
    #?juego([("piedra","papel"),("piedra","tijeras"),("piedra","lagarto")])
    #?juego([("papel","piedra"),("papel","tijeras"),("papel","lagarto")])
    #?juego([("tijeras","papel"),("tijeras","piedra"),("tijeras","lagarto")])
    #?juego([("lagarto","papel"),("lagarto","tijeras"),("lagarto","piedra")])
