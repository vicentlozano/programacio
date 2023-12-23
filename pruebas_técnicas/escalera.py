"""
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 """
numero_escalones = int(input("Introduce el numero de escalones, puede ser positivo o negativo: "))
def pintar_escalon(numero_escalones):
    if numero_escalones>0:
        escalon_ascendente = "_|"
        count = numero_escalones
        for i in range(0,numero_escalones):
            vacio = "  "
            print(vacio * count + escalon_ascendente)
            count -=1
    escalon1 = "_"
    escalon_descendente2 = "|_"  
    vacio = " "
    if numero_escalones<0:
       
        count = numero_escalones
        print(escalon1)
        for i in range(numero_escalones,0):
            
            print(vacio +escalon_descendente2)
            vacio= vacio + "  "

        
        
    if numero_escalones == 0:
        print("__")
        None
pintar_escalon(numero_escalones)