
#! Esto ejecuta la funcion hola, con un retardo de 5 segundos.
import threading
def hola():
    print("Hola!")
    
threading.Timer(5,hola).start()
#! Esto va a ejectar la funcion hola cada 5 segundos.\ ( despues de 
#! que pasen 10 segundos)
def holas():
    print("Holaaaaa!")
    threading.Timer(5,holas).start()
#! Esto hace que pasen 10 segundos antes de llamar a holas
threading.Timer(10,holas).start()