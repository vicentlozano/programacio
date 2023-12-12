"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 """
diccionarios = {}
def let(texto):
    leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
    texto = texto.upper()
    resultado = ""
    for char in texto:
        if char in leet:
            resultado += leet[char]
        else:
            resultado += char
    return resultado
            

"""Ahora vamos a ampliar esto para que el usuario puedo elegir su propio 
diccionario y tengo su propio lenguaje en clave,"""
def crear_diccionario():
    nombre = input("Introduce el nombre del diccionario: ")
    print("Los valores tienen que ser únicos para cada letra para que tenga sentido.")
    
   # diccionario[nombre] = 
    diccionario  = {"A": "", "B": "", "C": "", "D": "", "E": "", "F": "", "G": "", "H": "", "I": "",
            "J": "", "K": "", "L": "", "M": "", "N": "", "O": "", "P": "", "Q": "",
            "R": "", "S": "", "T": "", "U": "", "V": "", "W": "", "X": "", "Y": "", "Z": "",
            "1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "0": ""}
    #for i in diccionario[nombre]:
    #    diccionario[nombre][i] = (input("Introduce el valor de la letra " + i + ": "))
    #return 
    for i in diccionario:
        valor = input("Introduce el valor de la letra " + i + ": ")
        while valor in diccionario.values():
            print("El valor ya está en uso, por favor introduce otro.")
            valor = input("Introduce el valor de la letra " + i + ": ")
        diccionario[i] = valor
    diccionarios[nombre] = diccionario
    return diccionario
def codigosecreto(texto,diccionario):
    texto=texto.upper()
    resultado = ""
    for char in texto:
        if char in diccionario:
            resultado += diccionario[char]
        else:
            resultado += char
    return resultado
    
"""Estos métodos están muy bien , pero sin uno para descifrar el mensaje recibido
no valen para nadda, vamos a crearlo:"""
def obtener_clave(valor_buscado,diccionario):
    for clave, valor in diccionario.items():
        if valor == valor_buscado:
            return clave
    return None
def descifrar(texto,diccionario):
    
    resultado = ""
    for char in texto:
       if obtener_clave(char,diccionario) == None:
           resultado += char
       else:resultado += str(obtener_clave(char,diccionario))
    return resultado.lower()
#vamos a crear una función que nos permita comprovar que una letra o simbolo no este ya en el diccionario.

     
#menu

def menu():
    while True:
            print("\n1. Crear diccionario")
            print("2. Cargar diccionario")
            print("3. Descifrar")
            print("4. Codificar")
            print("5. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
               crear_diccionario()
               
            elif opcion == "2":
                None
                
            
            elif opcion == "3":
                diccionario_nombre = input("Introduce el nombre del diccionario: ")
                diccionario = diccionarios.get(diccionario_nombre)

                if diccionario is None:
                    print("No se encontró el diccionario.")
                    

                else:
                    # ahora puedes usar `diccionario` como un diccionario real
                    texto = input("Introduce el texto a descifrar: ")

                print(descifrar(texto, diccionario))
                
        
                
            elif opcion == "4":
                diccionario_nombre = input("Introduce el nombre del diccionario: ")
                diccionario = diccionarios.get(diccionario_nombre)

                if diccionario is None:
                    print("No se encontró el diccionario.")
                    

                else:
                    texto = input("Introduce el texto a codificar: ")
                    print(codigosecreto(texto, diccionario))
                  

            elif opcion == "5":
                print("¡Hasta luego!")
                
                exit()
            else:
                print("Opción no válida. Por favor, elige una opción del 1 al 5.")
                
menu()


    
    
