"""1. (2 puntos) Hacer una función a la que pasándole una letra del abecedario en castellano y una
cadena nos diga el número de veces que la letra aparece en la frase."""
import random
def numero_de_veces (letra,cadena):
    count=0
    for char in cadena:
        if char == letra:
            count = count+1
    return count
"""2. (2 puntos) Realizar una función que recupere una letra aleatoriamente del bombo teniendo en
cuenta que si la letra ha aparecido ya tres veces, no puede volver a aparecer"""
def recuperar_lletra(letras_salidas):
    abecedario2="abcdefghijklmnopqrstuvwyz"
    lletra_aleatoria = random.choice(abecedario2)
    while numero_de_veces(lletra_aleatoria,letras_salidas)>= 3:
        lletra_aleatoria = random.choice(abecedario2)
    letras_salidas= letras_salidas + lletra_aleatoria

    return lletra_aleatoria



    
   



"""3. (2 puntos) Hacer una función que diga si la frase que ha elegido el jugador es una frase válida,
debe tener al menos 10 letras sin contar los espacios en blanco y no repetir ninguna letra más de tres
veces"""
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def frase_valida(frase):
    abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    abecedario2="abcdefghijklmnopqrstuvwyz"
   
    if len(frase) - frase.count(' ')<10:
        return False
    
    for char in abecedario2:
        if numero_de_veces(char,frase)<=3:
            None
        else:
            return False 
    return True

"""4. (3 puntos) Hacer una función que compruebe si una frase es bingo, todas las letras de la frase se
encuentran en las letras extraídas y las que se repiten aparecen al menos, el mismo número de
veces."""
def esta_letra(letra,frase):
    for char in frase:
        if char == letra:
            return True
    return 
    
    
        
    
    
    

    
def bingo(frase,letras_extraidas):
    i = 0
    if frase_valida(frase)==False:
        print("frase no vàlida")
    else:
        for char in frase:
            if char == letras_extraidas[i]:
                i= i + 1
                
            else:
                print("No es bingo")
           
    
    
    
    
    
    
            
           

            

    
