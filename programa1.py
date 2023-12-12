#Exercici 1
numero = (int(input("escriu el número: ")))
if numero % 2 == 0:
    print("El número es parell")
#Exercici 2
import math
while True:
    radi = float(input("Escriu el radi: "))
    
    if radi > 0:
        area = 3.14 * radi**2
        print("El área del círcul és " +str(area))
        break
    else:
        print("El radi deu de ser un valor positiu. Torna a intentar-ho.")
#Exercici 3
any_de_naixement = (int(input("D'isme l'any de naixement: ")))
while any_de_naixement <0:
    any_de_naixement = (int(input("D'isme l'any de naixement: ")))
any_de_defuncio = (int(input("Disme l'any de defunció: ")))
while any_de_defuncio<any_de_naixement:
    print("Torna a provar") 
    any_de_defuncio = (int(input("D'isme l'any de defunció: ")))
print("fi del programa")
#Exercici 4 
numeros = int(input("Cuans números vols mostrar? "))
while numeros >=1:
    print(numeros)
    numeros = numeros-1
print("fi del programa")
#Exercici 5
valor_inicial=int(input("Escriu el valor inicial:"))
valor_final=int(input("Escriu el valor final:"))
increment=int(input("Escrui el increment:"))
if increment<0:
    while valor_inicial>=valor_final:
        print(valor_inicial)
        valor_inicial=valor_inicial+increment
else:
    while valor_inicial<=valor_final:
        print(valor_inicial)
        valor_inicial= valor_inicial+increment
print("fi del programa)")
#Exercici 6
a = int(9)
multiplicador=int(1)
while multiplicador<=10:
    print(a*multiplicador)
    multiplicador=multiplicador+1
#Exercici 7
numero=int(input("Escriu el numero i te dire cuans divisors té: "))
contador=int(0)

for i in range(1, numero+1):
    if(numero%i)==0:
        contador+=1
print(contador)
#Exercici 8
arrel_de_225=15
resposta=(int(input("Quina és l'arrel cuadrada de 225?: ")))
contador=0
while resposta!=arrel_de_225:
    contador=contador+1
    resposta=(int(input("Quina és l'arrel cuadrada de 225?: ")))
print("Les respostes errònies han sigut: "+str(contador))
#Exercici 9
primer=int(input("introdueïx el primer número: "))
segon= int(input("introdueïx el segòn número: "))
sumadeparells=0
sumadeimparells=0
if primer==segon:
    print("No hi ha cap número")
elif primer>segon:
    while primer>segon:
        primer=primer-1
        print(primer)
        if primer%2==0:
            sumadeparells=sumadeparells+primer
        else:
            sumadeimparells=sumadeimparells+primer
else:
    while primer<segon:
        primer=primer+1
        print(primer)
        if primer%2==0:
            sumadeparells=sumadeparells+primer
        else:
            sumadeimparells=sumadeimparells+primer
print("La suma dels parrels és: "+str(sumadeparells))
print("la suma de imparells és: "+str(sumadeimparells))
#Exercici 10
valor_a=int(input("Intrdueïx el valor a, que ha de ser menor que el b: "))
valor_b=int(input("introdueïx el valor b (recorda que ha de ser major que a):"))
if valor_a>=valor_b:
    print("Has introduït mal els valors, reinicia el programa i torna a intentar-ho")
else:

    while valor_a<=valor_b:
        valor_a=valor_a+2
        valor_b=valor_b-3
        print("valor a: "+str(valor_a))
        print("valor b: "+str(valor_b))
#Exercici 11
n = int(input(" Escriu un número n: "))

acumulador = 0  

for i in range(1, n + 1):
    acumulador += i  
    expresion = '+'.join(map(str, range(1, i + 1)))
    print(f"{expresion}={acumulador}")
#Exercici 12
base=int(input("Introdueïx la base: "))
exponent=int(input("Intrdueïx el exponent: "))
resultat=base**exponent
print("El resultat és: "+str(resultat))
#Exercici13

resultat=1
for numero in range(1,41):
    if numero%2 !=0:
        print(numero)
        resultat*=numero
    
print("el resultat dels números impars del 1 al 40 són: ", resultat)
#Exercici 14
suma=0
producte=1
mitjana=0
for numero in range(1,101):
    suma+=numero
print("La suma de tots els números és ",suma)
mitjana=suma//100
print("la mitjana és: ",mitjana)
for numero in range (1,101):
    producte*=numero
print("El producte és: ",producte)
#Exercici 15
numero=int(input("Introdueïx un número: "))
factorial=1

for i in range(1, numero + 1):
        factorial *= i
print("El factorial és: ",factorial)
#Exercici 16
numero = int(input("Escriu un número: "))

if numero <= 1:
    es_primo = False
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es un número primer.")
else:
    print(f"{numero} no es un número primer.")
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
    
#Exercici18
for numero in range(1,11):
    multiplicador=int(1)
    while multiplicador<=10:
        print(numero*multiplicador)
        multiplicador=multiplicador+1







