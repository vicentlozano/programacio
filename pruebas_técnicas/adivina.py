""" 5 x 6 huecos , verde bien, amarillo esta pero no es su posicion, azul no estan.
solo hay que acertar una palabra.
6 intentos.
todas las palabras seran de 5 letras, con una tematica al azar.
"""
import random
import colorama
from colorama import Fore, Back, Style
from colorama import Fore
import nltk
nltk.download('cess_esp')
from nltk.corpus import cess_esp



colorama.init(autoreset=True)
tablero = []
tablero = [["🔲" for _ in range(5)] for _ in range(6)]  # Crear el tablero
"""Este fragmento de código crea una lista de listas en Python, que se puede visualizar como un tablero o una matriz. Aquí está lo que hace cada parte:

"🔲" for _ in range(5): Este es un bucle for en una comprensión de lista que crea una lista de cinco elementos, donde cada elemento es el string "🔲". El _ es una convención que se usa cuando no necesitas el valor del índice en el bucle.

["🔲" for _ in range(5)] for _ in range(6): Este es otro bucle for en una comprensión de lista que crea una lista de seis elementos, donde cada elemento es la lista creada en el paso anterior. Por lo tanto, obtienes una lista de seis listas, donde cada lista contiene cinco cuadros blancos "🔲".

tablero = ...: Finalmente, la lista de listas se asigna a la variable tablero.

Por lo tanto, tablero es una lista de seis listas, donde cada lista contiene cinco cuadros blancos "🔲". Esto se puede visualizar como un tablero o una matriz de 6x5, donde cada celda contiene un cuadro blanco "🔲"."""
def elegir_palabra():
    #palabras = ["perro", "raton", "color", "silla", "libro", "pluma", "papel", "verde", "palco", "cable"]
    palabras = cess_esp.words()
    palabra = random.choice(palabras)
    while len(palabra) != 5 or palabra.isalpha() == False:
        palabra = random.choice(palabras)
    return palabra
# Crear el tablero fuera de la función
palabra = elegir_palabra()
tablero = [["🔲" for _ in range(5)] for _ in range(6)]
intentos = 0


def pintar_letra(palabra_introducida,palabra,intentos,tablero):
    if palabra_introducida == palabra: 
        palabra  = list(palabra)
        palabra_introducida = list(palabra_introducida)
        for i in range(len(palabra_introducida)):
            palabra_introducida[i] = Fore.GREEN + palabra_introducida[i].center(3)
        primera_fila = tablero[intentos]
        for i in range(len(palabra_introducida)):
            primera_fila[i] = palabra_introducida[i]
        for fila in tablero:
            print(' '.join(fila))


        return True, intentos,tablero
    else:
        palabra  = list(palabra)
        palabra_introducida = list(palabra_introducida)
        if len(palabra_introducida) != len(palabra):
            print("Por favor, introduce una palabra de la misma longitud.")
            return False, intentos, tablero

        for i in range(len(palabra_introducida)):
            if palabra_introducida[i] == palabra[i]:
                # Esta letra ira en verde.
                palabra_introducida[i] = Fore.GREEN + palabra_introducida[i].center(3)
            elif palabra_introducida[i] in palabra:
                # Esta letra ira en amarillo
                palabra_introducida[i] = Fore.YELLOW + palabra_introducida[i].center(3)
            else:
                # Esta palabra ira en azul
                palabra_introducida[i] = Fore.BLUE + palabra_introducida[i].center(3)
        
        

        primera_fila = tablero[intentos]
        for i in range(len(palabra_introducida)):
            primera_fila[i] = palabra_introducida[i]
        for fila in tablero:
            print(' '.join(fila))
        
        intentos += 1
        return  False,intentos,tablero


def juego():
    contador = 0
    palabra = elegir_palabra()
    tablero = [["🔲" for _ in range(5)] for _ in range(6)]  # Definir tablero aquí
    print("Bienvenido al juego de adivinar palabras, tienes 6 intentos para adivinar la palabra, suerte!")
    print("La palabra tiene 5 letras, y es una palabra en español.")
    for fila in tablero:
            print(' '.join(fila))

    while contador <= 5:
        palabra_introducida= str(input("Escribe la palabra: "))
        palabra_introducida = palabra_introducida.lower()
        resultado, contador, tablero = pintar_letra(palabra_introducida, palabra, contador, tablero)
        if resultado:
            
            print("Has acertado, enorabuena!")
            respuesta = input("Quieres volver a jugar? S/N: ")
            respuesqta = respuesta.upper()
            
            if respuesta == "S":
                juego()
            else: 
                break
        elif contador >5 :
            print("Has perdido, la palabra era: ",palabra)
            respuesta = input("Quieres volver a jugar? S/N: ")
            respuesqta = respuesta.upper()
            
            if respuesta == "S":
                juego()
            else: 
                break
juego()



    