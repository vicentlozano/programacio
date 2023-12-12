import random
con_sin_numeros = True
con_sin_simbolos = True
mayuscula = True


def generador ():
    numeros = int(input("¿Cuántos números quieres que tenga tu contraseña? ")) 
    while numeros <8 or numeros >16:
        print("Error, la contraseña debe tener entre 8 y 16 caracteres")
        numeros = int(input("¿Cuántos números quieres que tenga tu contraseña? ")) 
    mayuscula = input("¿Quieres que tu contraseña tenga mayúsculas? (S/N) ")
    while mayuscula != "S" and mayuscula != "N":
        print("Error, introduce S o N")
        mayuscula = input("¿Quieres que tu contraseña tenga mayúsculas? (S/N) ")
    if mayuscula == "S":
        mayuscula = True
    elif mayuscula == "N":
        mayuscula = False
    con_sin_numeros = input("¿Quieres que tu contraseña tenga números? (S/N) ")
    while con_sin_numeros != "S" and mayuscula != "N":
        print("Error, introduce S o N")
        con_sin_numeros = input("¿Quieres que tu contraseña tenga números? (S/N) ")
    if con_sin_numeros == "S":
        con_sin_numeros = True
    elif con_sin_numeros == "N":
        con_sin_numeros = False
    con_simbolos = input("¿Quieres que tu contraseña tenga símbolos? (S/N) ")
    while con_simbolos != "S" and mayuscula != "N":
        print("Error, introduce S o N")
        con_simbolos = input("¿Quieres que tu contraseña tenga símbolos? (S/N) ")
    if con_simbolos == "S":
        con_sin_simbolos = True
    elif con_simbolos == "N":
        con_sin_simbolos = False
    numerosaleatorios = [1,2,3,4,5,6,7,8,9,0]
    simbolos = ["!","@","#","$","%","&","/","(",")","=","?","¡","¿","*","-","+","<",">"]
    """letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ",
              "o","p","q","r","s","t","u","v","w","x","y","z"]"""
    #? Mejor con range y chr?
    #! Habria que hacer un random de 97 a 122 y luego convertirlo a letra
    letras = list(range(97,123))
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ",
                  "O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    contraseña = [] 
    for i in range(numeros):
        while len(contraseña) < numeros:
            option = random.randint(1,4)
            if option == 1 and con_sin_numeros == True:
                contraseña.append(random.choice(numerosaleatorios))
            if option == 2 and mayuscula == True:
                contraseña.append(random.choice(mayusculas))
            if  option == 3 and con_sin_simbolos == True:
                contraseña.append(random.choice(simbolos))
            if option == 4 : contraseña.append(chr(random.choice(letras))) 
            #! Random de 97 a 123 pasado por chr que convierte asci a caracter.
    random.shuffle(contraseña)
    print("Tu contraseña es: " + "".join(map(str, contraseña)))
generador()