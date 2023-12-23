""" Exercici proposat 1:
    Fes un programa que, donades 2 varialbes enteres, mostre quin
    és el número més gran i quin el més menut."""

variable_1 = int(input("Introdueix la primera variable: "))
variable_2 = int(input("Introdueix la segona variable: "))
if variable_1 < variable_2:
    print("El número més gran és: 3" + str(variable_2) +  ", i el més xicotet és: "+ str(variable_1)+".")
if variable_1 > variable_2:
   print("El número més gran és: " + str(variable_1) +  ", i el més xicotet és: "+ str(variable_2)+".")
elif variable_1 == variable_2:
    print("Ambdós números són iguals.")

""" Exercici proposat 2:
    Quin és el resultat de les següents expressions? 
    Indica també si hi ha pèrdua o promoció d'informació.

1. int a = 3/5 + 0.75/2; El resultat no es un enter, el idoni sería un double, perqué té 3 decimals: 0.375. Hi hauria pèrdua d'informació.
2. float b = 50/2 + 7%3; En aquest cas el resultat es 26, amb un int ens vindria milor. Hi ha promococió de informació.
3. int c = 1.75E9; Pèrdua d'informació. Deuría ser un double.
4. int b = 5/2 + 6.5/2; Pèrdua d'informació. Deuría ser un double. ( 5.25)
5. float c = 2.5E-125; Pèrdua de informació. Deuría ser un double.
6. int d = 0.5E10; Hem introduït un decimal a un Int. No és correcte dpenent del tipat del llengüatge. El resultat és un nombre enter.
7. long e = -23; És correcte. Es una promoció de d'informació.

"""
""" Exercici proposat 3: 
    Fes un programa que pregunte quants anys té algú iq ue mostre per pantalla la quantitat d'anys que falten per a la majoria
    d'edat i per a jubilar-se."""

anys = int(input("Quants anys tens?: "))
while anys < 0 :
   anys = int(input("Torna a introduïr una edad vàlida: "))
major_de_edat= bool
anys_restants_jubilació = 67 - anys
if anys >= 18:
    major_de_edat=True
else:
    major_de_edat=False
if major_de_edat==False:
    print("Tens "+ str(anys)+ " anys. No eres major d'edat i et queden "+ str(anys_restants_jubilació) + " anys per a jubilarte.")
if major_de_edat==True:
    print("Tens "+ str(anys)+ " anys. Eres major d'edat i et queden "+ str(anys_restants_jubilació) + " anys per a jubilarte.")

""" Exercici 4:
    Programa que pregunte per la basei l'altura d'un triangle i mostre per pantalla l'àrea d'eixe triangle."""

base_triangle = float(input("Dis-me la base del triangle: "))
while base_triangle < 0:
    base_triangle = float(input("Tornma'm a dir una base vàlida: "))
altura_triangle = float(input("Dis-me l'altura del triangle: "))
while altura_triangle < 0:
    altura_triangle = float(input("Tornma'm a dir una altura vàlida: "))
area_triangle = base_triangle * altura_triangle
print("L'àrea del triangle és: "+ str(area_triangle)+ ".")

""" Exercici proposat 5:
    A partir d'aquest programa en el qual hem escrit els blancs per a formatar el text, 
    escriu-lo per a aconseguir el mateix per pantalla però fent servir les funcions estudiades al tema."""
llibre1="llibre"
escritor1="autor"
llibre2="El Quijote"
escritor2="Cervantes"
llibre3="Harry Potter y las Reliquias"
escritor3="JK Rowling"
llibre4="Carlos en tu cocina"
escritor4="karlos Arguiñano"
print(llibre1.ljust(60,"_") + escritor1.rjust(60,"_"))
print(llibre2.ljust(60,"_") + escritor2.rjust(60,"_"))
print(llibre3.ljust(60,"_") + escritor3.rjust(60,"_"))
print(llibre4.ljust(60,"_") + escritor4.rjust(60,"_"))

""" Exercici proposat 6:
    A partir del llistat de números que tens a continuació, imprimir-los ordenats
    pel punt decimal i amb dos decimals."""
print("%7.2f %7.2f %7.2f %7.2f %7.2f"%(23.453,2.324,154,23142.253,53.0000343))
# Com no sabia si ho volies tot a una línea , els he posat separats també.
print("%8.2f"%23.453)
print("%8.2f"%2.324)
print("%8.2f"%154)
print("%8.2f"%23142.253)
print("%8.2f"%53.0000343)

    