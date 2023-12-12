"""1. Fes un programa que calcule l’import a pagar per un vehicle al circular per una autopista. El
vehicle pot ser una bicicleta, una moto, un cotxe o un camió. L’import es calcularà segons les
següents dades:
• Un import fix de 100 unitats per a les tots els vehicles.
• Les motos i els cotxes pagaran a demés 30 unitats per km.
• Els camions pagaran 30 unitats per km més 25 unitats per cada Tm."""

# Exercici 1:
print("1. bicicleta")
print("2. moto")
print("3. cotxe")
print("4. camió")
print("5. eixir")
opcio = int(input("Selecciona opció: "))
while opcio < 1 or opcio > 5:
    opcio = int(input("Selecciona una opció vàlida: "))
if opcio == 4:
    datos = input("Kilòmetres i tones: ")
    km, tn = map(float, datos.split())
    total = 100 + 30*km + 25*tn
    print("Import = " + str(total))
elif opcio in [2,3]:
    km = float(input("Kilòmetres: "))
    total = 100 + 30*km
    print("Import = " + str(total))
elif opcio == 1:
    print("Import = 100")
else:
    total = 0

# Exercici 2:
n = int(input("Introduïx un enter: "))
c = str(input("Introduïx un caràcter qualsevol (*,€,@ o una lletra): "))
count = n
while count>0:
    print(c*n)
    count -= 1

# Exercici 3:

#funció x * -2x = n
x = 10
print("Costat1".ljust(30," ") + "Costat2" + "Area".rjust(30," "))
while x <= 30:
    n = 100 - 2*x
    area = x * n
    costat1 = str(x)
    costat2 = str(n)
    area = str(area)
    print(costat1.ljust(30, " ") + costat2 + area.rjust(30," "))
    x += 1
print("L'àrea màxima és 1250, per a uns costats de 25 i 50.")



    


