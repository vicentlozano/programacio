#Exercicis bifurccions
"""1. Fes un programa que, donades 2 variables enteres, mostre quin és el número més gran i quin el
més menut.
2. Fes un programa que, donades 3 variables enteres, mostre quin és el número més gran.
3. Fes un programa que pregunte quants anys té algú i que mostre per pantalla la quantitat d’anys
que li falten per a la majoria d’edat i per a jubilar-se.
4. El servei d’endocrinologia de l’Hospital de La Ribera necessita un programa que calcule el pes
recomanat d’una persona. Escriu un programa que llija l’altura en metres i l’edat d’una persona i
mostre el seu pes recomanat segons la fórmula pes = (altura_en_cm – 100 + 10%edat) * 0.9.
5. Fes un programa que calcule les solucions reals de l’equació de 2n grau ax2 + bx + c = 0, amb
la famosa fórmula
x =
−b ±
√
b
2 − 4ac
2a"""
#exercici 1
variable_1 = int(input("Introduïx el primer número(enter): "))
variable_2 = int(input("Intrdueïx el segón número(enter): "))

if variable_1 > variable_2:
    print("el primer número: " + str(variable_1) , ", és més gran que el segón: " + str(variable_2))
elif variable_1 == variable_2:
    print("Els dos números: " + str(variable_1) , "i " + str(variable_2), " són iguals")
else:
    print("el segón número: "  + str(variable_2) , ", és més gran que el primer: " + str(variable_1))

#exercici 2
variable_1 = int(input("Introduïx el primer número(enter): "))
variable_2 = int(input("Intrdueïx el segón número(enter): "))
variable_3 = int(input("Introduïx el tercer número(enter): "))
lista = [variable_1,variable_2,variable_3]
lista.sort()
gran = lista.pop()
print("el número més gran és ",gran)

#exercici 3
edad = int(input("Dis-me la teua edat: "))
major_de_edad = bool
anys_per_jubilarse = 65 - edad
if edad < 18:
    major_de_edad = False
else:
    major_de_edad = True
if major_de_edad == True:
    print("Eres major d'dedat i et queden " +str(anys_per_jubilarse),  " anys per a jubilarte.")
else:
    print("Eres menor d'dedat i et queden " +str(anys_per_jubilarse),  " anys per a jubilarte.")

#exercici 4 (altura_en_cm – 100 + 10%edat) * 0.9.

altura_en_metres = float(input("Introduïx la teua altura en metres: "))
altura_en_cent = altura_en_metres*100
edat = int(input("Introduïx la teua edat: "))
pes_recomanat = (altura_en_cent - 100 + 10%edat)* 0.9
print(str(pes_recomanat))

#exercici 5
equació_1 = "ax2 + bx + c = 0"

from math import sqrt

def calcula_solucions_quadratiques(a, b, c):
    # Calculamos el discriminante
    discriminant = b**2 - 4*a*c

    # Verificamos si el discriminante es negativo
    if discriminant < 0:
        return None  # No hay soluciones reales

    # Calculamos las dos soluciones utilizando la fórmula cuadrática
    solucio1 = (-b + sqrt(discriminant)) / (2*a)
    solucio2 = (-b - sqrt(discriminant)) / (2*a)

    return solucio1, solucio2

# Ejemplo de uso
a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))

soluciones = calcula_solucions_quadratiques(a, b, c)

if soluciones is None:
    print("La ecuación no tiene soluciones reales.")
else:
    print(f"Las soluciones de la ecuación son {soluciones[0]} y {soluciones[1]}")
#Exercicis bucles
"""1. Programa que mostre la taula de multiplicar del 9.
2. Programa que demane una taula de multiplicar i la mostre.
3. Programa que mostre les taules de multiplicar del 2 al 9.
Nota: este exercici és més difícil, ja que suposa incloure un bucle dins d’altre.
4. Programa que faça una quiniela aleatòria (busca a Internet com trobar números aleatoris en
Python). El programa haurà de mostrar quin símbol posem en cadascuna de les 15 posicions (1,
X o 2):"""

#exercici 1
a = 1
b = 9
while a <= 10:
    print(a*b)
    a += 1

#exercici 2
def taula_de_multiplicar(a):
    b = 1
    while b <= 10:
        print(a * b)
        b += 1
       
    return 
#exemple:
a = int(input("Introduïx el número del que vols saber la taula: "))
print(taula_de_multiplicar(a))

#exercici 3

a = 0
b = 2
count = 2
while count <= 9:
    
    while a <= 10:
        print(b*a)
        a += 1
    count += 1