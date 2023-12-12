from datetime import datetime

def num_pseudoaleatorio():
    ahora  = datetime.now()
    nuemero  = ahora.microsecond *1000
    strnum_aleatorio = []
    numaleatoria = []
    for char in str(nuemero):
        strnum_aleatorio.append(int(char))
    if len(strnum_aleatorio) >= 4:
        numaleatoria.append(strnum_aleatorio[2])
        numaleatoria.append(strnum_aleatorio[3])
        
    else:
        return None


    resultado = str(numaleatoria[0]) + str(numaleatoria[1])
    suma = int(resultado)
    if suma < 100 and suma > 0 and suma in range(95,100) and (ahora.microsecond %2 == 0): suma += 1
    print(suma)
num_pseudoaleatorio()
    
   
    

#!Comprovación de que todos los números del 0 al 100 están en el conjunto
"""resultados=[]
num_pseudoaleatorio()
for _ in range(100000):
    resultados.append(num_pseudoaleatorio())
resultados = set(resultados)

# Verificar si todos los números del 0 al 100 están en el conjunto
for i in range(101):
    if i not in resultados:
        print(f"El número {i} no fue generado.")"""
    