# 1. Fer un programa que llija dos números enters i mostre la suma dels dos, tal com es veu.

primer_sumando = int(input("Introduce el primer sumando: "))
segundo_sumando = int(input("Introduce el segundo sumando: "))
suma = primer_sumando + segundo_sumando
print("La suma de " + str(primer_sumando) + " y " + str(segundo_sumando) + " es " + str(suma))

# 2. Donades dues variables a i b reals, fer un programa que intercanvie els valors de les mateixes.

#Primer mètode:
variable_a = float(input("Introduce el valor de la variable a: "))
variable_b = float(input("Introduce el valor de la variable b: "))
print("El valor de a es " + str(variable_b))
print("El valor de b es " + str(variable_a))

#Segon mètode:
variable_a = float(input("Introduce el valor de la variable a: "))
variable_b = float(input("Introduce el valor de la variable b: "))
ext1=variable_a
ext2=variable_b
variable_a=ext2
variable_b=ext1
print("El valor de a es " + str(variable_a))
print("El valor de b es " + str(variable_b))

#Tercer métode:
variable_a = float(input("Introduce el valor de la variable a: "))
variable_b = float(input("Introduce el valor de la variable b: "))
variable_a, variable_b = variable_b, variable_a
print("El valor de a es " + str(variable_a))
print("El valor de b es " + str(variable_b))


#Exercici 3: Fer un programa donades 3 variables(del tipus que siguin) intercanvie els seus valors de la següent manera.
# b tome el valor de a, 
# c tome el valor de a , y 
# a tome el valor de c.
# ( Sin variables auxiliares )
a = (input("Ingrese  el valor de a: "))
b = (input("Ingrese  el valor de b: "))
c = (input("Ingrese  el valor de c: "))
a, b, c = c, a, a
print("a= " + str(a))
print("b= " + str(b))
print("c= " + str(c))

#Exercici 4: Fer un programa que demane 4 números reals i faça la suma, mostrant-la per pantalla amb 3 decimals.
numero1 = float(input("Escriu el primer número: "))
numero2 = float(input("Escriu el segon número: "))
numero3 = float(input("Escriu el tercer número: "))
numero4 = float(input("Escriu el quart número: "))
suma = numero1 + numero2 + numero3 + numero4
print("La suma és: %5.3f"%suma)


#Exercici 5: Fer un programa que demane 2 números i mostre per pantalla la suma, resta producte i divisió amb 4 decimals.

numero1 = float(input("Escriu el primer número: "))
numero2 = float(input("Escriu el segon número: "))
suma = numero1 + numero2
resta = numero1 - numero2
divisio = numero1 / numero2
print("La suma és: %5.4f"%suma)
print("La resta és: %5.4f"%resta)
print("La divisio és: %5.4f"%divisio)

#Exercici 6: Afegir a l'anterior programa el càlcul de la divisió entera i el residu.

numero1 = float(input("Escriu el primer número: "))
numero2 = float(input("Escriu el segon número: "))
suma = numero1 + numero2
resta = numero1 - numero2
divisio = numero1 / numero2
divisio_entera = numero1 // numero2
residu  = numero1 % numero2
print("La suma és: %5.4f"%suma)
print("La resta és: %5.4f"%resta)
print("La divisio és: %5.4f"%divisio)
print("La divisio entera és: %5.4f"%divisio_entera)
print("El residu és: %5.4f"%residu)

#Exercici 7: Implementar un programa que calcule la temperatura en graus Celsius a partir de la temperatura en graus
#            Fahrenheit. La fòrmula es la següent: C= (5/9(F-32))

temperatura_fahrenheit = float(input("Introdëix la temperatura en graus Fahrenheit: "))
temperatura_celsius = (5/9)*(temperatura_fahrenheit - 32)
print("La temperatura en graus Celsius és: " + str(temperatura_celsius))

#Exercici 8: Implementar un programa que calcule els interessos prodüits i el capital d'una quantitat c invertida a un interés r 
#            (expressat en tant per cent) durant t dies. La fórmula per al càlcul d'interessos és: I = (c * r * t)/(360 * 100)

c = float(input("Introdüeix el capital: "))
r = float(input("Introdüeix el interés: "))
t = float(input("Introdüeix els dies: "))
i = ( c * r * t)/(360 * 100)
capital_acumulat = i + c
print("Aquests són els interessos: " + str(i) + ". El capital acumulat és: " + str(capital_acumulat))

#Exercici 9: Calcula el valor del polinomi: ax^5 -5x^3 +2x -7.

# Defineix el valor de x
x = 2  # Pots canviar aquest valor pel que vulguis
a = 3

# Calcula el valor del polinomi
resultat = (a * x**5) - (5 * x**3) + (2 * x) - 7

# Imprimeix el resultat
print("El valor del polinomi és:", resultat)

#Exercici 10: Calcula el valor del polinomi: ax^5 -bx^3 + cx -d, sent a, b, c i d variables
#             introdüides per teclat. Comprova els valors amb l'exercici 9

# Defineix el valor de x
x = 2  # Pots canviar aquest valor pel que vulguis
a = int(input("Intrdüeix el valor de a:  "))
b = int(input("Intrdüeix el valor de b:  "))
c = int(input("Intrdüeix el valor de c:  "))
d = int(input("Intrdüeix el valor de d:  "))


# Calcula el valor del polinomi
resultat = (a * x**5) - (b * x**3) + (c * x) - d

# Imprimeix el resultat
print("El valor del polinomi és:", resultat)







