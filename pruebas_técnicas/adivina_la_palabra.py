"""
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 """
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
#! Lo plantearemos de tres formas; una con una lista, otra con una clase y otra con un diccionario(seguramente sea la mas fácil)
lista_de_palabras=["puerta","teclado","pantalla","cable","cargador","cristal","libro","tijeras","pintar","papel","raton","ordenador","mesa","silla","ventana","cortina","cama","armario","cajonera","estanteria","cuadro","pintura","pintar","pincel","lapiz","boligrafo","goma","sacapuntas","sobre","carta","sello","buzon","telefono","movil","movil","telefono","telefono","telefono","telefono","telefono","telefono","telefono","telefono"]
def elejir_palabra():
    palabra = random.choice(lista_de_palabras)
    return palabra

def ocultar_palabra(palabra):
    palabra = list(palabra)
    caracteres_a_tapar = int (len(palabra)* 0.6)
    signo_oculto = "_"
    caracteres_ocultos = 0
    while caracteres_ocultos < caracteres_a_tapar:
        indice = random.choice(range(len(palabra)))
        if  palabra[indice] != signo_oculto:
            palabra[indice] = signo_oculto
            caracteres_ocultos +=1
    palabra_oculta =''.join(palabra)
    return  palabra_oculta
def cambiar_caracter(respuesta,palabra,palabra_oculta):
    palabra_oculta = list(palabra_oculta)
    palabra = list (palabra)
    for i in range(len(palabra)):
        if respuesta == palabra[i]:
            palabra_oculta[i]= respuesta
    palabra_oculta = ''.join(palabra_oculta)
    palabra = ''.join(palabra)
    return palabra_oculta


   
def comprobar (respuesta,palabra,palabra_oculta,boola):
    
    
    if len(respuesta) == len(palabra)  or len(respuesta) == 1:
        if respuesta == palabra:
            print("HAS ACERTADO!🖐️")
            boola = True
            y_n=input(Fore.LIGHTWHITE_EX +"Quieres jugar otra partida?: Escribe S para si, y N para no: ")
            if y_n.upper() == "S":
                juego()
            else: exit()

        elif respuesta in palabra and len(respuesta)==1:
            palabra_oculta = cambiar_caracter(respuesta,palabra,palabra_oculta)
            if palabra_oculta == palabra:
                boola = True
                print(palabra)
                print("HAS ACERTADO!🖐️")
                y_n=input(Fore.LIGHTWHITE_EX +"Quieres jugar otra partida?: Escribe S para si, y N para no: ")
                if y_n.upper() == "S":
                    juego()
                else: exit()

        




                   


            
        
           
            
       
    return  palabra_oculta,boola
def juego():
    cont= 10
    boola = False
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX +"🤔Esto es un pequeño juego que consista en adivinar palabras en 10 intentos.\n🤔El juego comienza proponiendo una palabra aleatoria incompleta.\n🤔Por ejemplo \"m_ur_d_v\", y el número de intentos que le quedan\n🤔El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que la palabra a adivinar)\n🤔Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta uno al número de intentos\n🤔Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno al número de intentos\n🤔Si el contador de intentos llega a 0, el jugador pierde")
    palabra = elejir_palabra() 
    palabra_oculta = ocultar_palabra(palabra)
    print(Style.BRIGHT + "La palabra oculta és: "+ palabra_oculta)
    
    while cont > 0 and boola == False :
        respuesta = str(input(Style.DIM + Fore.LIGHTCYAN_EX +"Escribe la respuesta, recuerda que solo puedes introducir una letra sola para resolver un hueco, o toda la palabra: " ))
        palabra_oculta,boola  = comprobar(respuesta,palabra,palabra_oculta,boola)
        if boola == True:
            break
       
        cont -=1
        print(Fore.LIGHTRED_EX +"Te quedan "+ str(cont)+ " intentos.\n "  + palabra_oculta)
        if cont == 0: 
            print(Fore.LIGHTMAGENTA_EX +"Has perdido!😅.")
            y_n=input(Fore.LIGHTWHITE_EX +"Quieres jugar otra partida?: Escribe S para si, y N para no: ")
            if y_n.upper() == "S":
                juego()
            else: exit()



    
juego()
    


