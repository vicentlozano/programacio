"""
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 """
import time
import timer
numero_inicial= int(input("Desde que numero quieres empezar?: "))
while numero_inicial <=0:
     numero_inicial = int (input("Vuelve a introducir un numero entero positivo, por favor: "))
segundos_transcurridos= int(input("Quantos segundos pasan entre numero y numero?: "))
while segundos_transcurridos <=0:
     segundos_transcurridos = int (input("Vuelve a introducir un numero entero positivo, por favor: "))
def cuenta_atras(numero_inicial, segundos_transcurridos):
    while numero_inicial >=0:
        print(numero_inicial)
        numero_inicial -=1
        time.sleep(segundos_transcurridos)
   
        
cuenta_atras(numero_inicial,segundos_transcurridos)
