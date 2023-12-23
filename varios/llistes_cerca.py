import random
            
llista = [1, 3, 5, 9, 7, 3, 9, 10]
llista2 = [1, 4, 5, 2, 3, 5, 3, 2]

def esta_en_la_llista(lista, numero):
    count = 0
    longitud = len(lista)
    
    while count < longitud:
        if lista[count] == numero:
            print("El número " + str(numero) + " está en la lista")
            return True
        count += 1
    
    print("El número " + str(numero) + " no está en la lista")
    return False            
            
"ahora intentaremos decir las veces que se repite"
def esta_i_posicio_es_repeteox (lista, numero):
    count = 0
    longitud = len(lista)
    posicio = ""
    vegades_repetit= 0
    esta = False
    
    while count < longitud:
        if lista[count] == numero:
            posicio = posicio + str(count) + " "
            vegades_repetit = vegades_repetit + 1
            esta = True
        count += 1
        

    if esta == True:
            return  print("el numero "+ str(numero)+ " esta en la llista. S'ha repetit "+ str(vegades_repetit) + " vegades i está en la posició: "+ posicio)
    else:
         print("El número " + str(numero) + " no está en la lista")
"ordenar llista"
llista2.sort()
"llistes amb strings"
lista1=["dilluns", "dimarts", "dimecres", "dijous", "divendres"]
concatenar = ""
minuts_correr = 0
plou = False
def calendari_correr_i_oratge_aleatori():
     lista1=["dilluns", "dimarts", "dimecres", "dijous", "divendres"]
     concatenar = ""
     minuts_correr = 0
     plou = False
     for dia in lista1:
          plou=random.choice([True,False])
          if plou == True:
               concatenar += dia + " no correrem\n"
          else:
               minuts_correr = random.randrange(1,10)
               concatenar += dia +" correrem " + str(minuts_correr) + " minuts\n"
     print(concatenar)
               

    
def calendari_correr_i_oratge_ale5atori():
    lista1=["dilluns", "dimarts", "dimecres", "dijous", "divendres"]
    concatenar = ""
    minuts_correr = 0
    plou = False
    for dia in lista1:
        plou = random.choice([True, False])
        if plou:
            concatenar += dia + " no correrem\n"
        else:
            minuts_correr = random.randrange(1, 10)
            concatenar += dia + " correrem " + str(minuts_correr) + " minuts\n"

    print(concatenar)
def restar_1 (num):
    num = num -1
    return num
def sumar_1(num):
     num = num + 1
     return num
                







