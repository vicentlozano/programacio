def sombrero_seleccionador():
    #! Necesito que no me insinues cosdigos de la solucion, solo que me digas si voy bien o mal.
    #* Las casas son: Gryffindor, Hufflepuff, Ravenclaw y Slytherin.
    #? Ahora plantearemos 5 preguntas por pantalla, que tendrán 4 posibles respuestas a elegir en la terminal.
    """? Las preguntas seran:
     *Con que fin estudias magia? -
       Ayudar a los demás Hufflepuff
       Para ser famoso      Gryffindor
       Para ser poderoso    Slytherin
       Para ser feliz    Ravenclaw
     * Dada la opción, preferirías inventar una poción que garantizara:
        Gloria            Gryffindor
        Sabiduria      Ravenclaw
        Amor        Hufflepuff
        Poder           Slytherin
     * ¿Cómo le gustaría ser conocido en la historia?
        El sabio        Ravenclaw
        El bueno    Hufflepuff
        El gran       Gryffindor
        El audaz    Slytherin
     *¿Que camino te tienta más?
        El carril amplio, soleado y cubierto de hierba   Hufflepuff
        El callejón estrecho, oscuro e iluminado por linternas  Slytherin
        El camino retorcido y cubierto de hojas a través del bosque  Ravenclaw
        La calle adoquinada bordeada de edificios antiguos  Gryffindor
     *Una vez cada siglo, el arbusto Flutterby produce flores que adaptan su aroma para atraer a los desprevenidos. Si te atrajera, olería a:
        Una chimenea crepitante Gryffindor
        Pergamino fresco        Ravenclaw  
        Tu hogar    Hufflepuff
        El mar   Ravenclaw
      """
    #? Ahora plantearemos 5 preguntas por pantalla, que tendrán 4 posibles respuestas a elegir en la terminal.
    #! Segun la respuesta de cada pregunta, se le sumara un valor a cada casa.
    #! Al final, se mostrara la casa con mas puntos.
    Gryffindor = 0
    Hufflepuff = 0
    Ravenclaw = 0
    Slytherin = 0
    print("Con que fin estudias magia? \n 1.Ayudar a los demás \n 2.Para ser famoso   \n 3.Para ser poderoso   \n 4.Para ser feliz")
    respuesta1 = int(input("Escribe el numero de la respuesta: "))
    while respuesta1 not in range(1,4):
        if respuesta1 == 1:
            Hufflepuff += 1
        elif respuesta1 == 2:
            Gryffindor += 1
        elif respuesta1 == 3:
            Slytherin += 1
        elif respuesta1 == 4:
            Ravenclaw += 1
        else:
            print("No es una respuesta valida")
    print("Dada la opción, preferirías inventar una poción que garantizara: \n 1.Gloria \n 2.Sabiduria \n 3.Amor \n 4.Poder")
    respuesta2 = int(input("Escribe el numero de la respuesta: "))
    while respuesta2 not in range(1,4):
        if respuesta2 == 1:
            Gryffindor += 1
        elif respuesta2 == 2:
            Ravenclaw += 1
        elif respuesta2 == 3:
            Hufflepuff += 1
        elif respuesta2 == 4:
            Slytherin += 1
        else:
            print("No es una respuesta valida")
    print("¿Cómo le gustaría ser conocido en la historia? \n 1.El sabio \n 2.El bueno \n 3.El gran \n 4.El audaz")
    respuesta3 = int(input("Escribe el numero de la respuesta: "))
    while respuesta3 not in range(1,4):
        if respuesta3 == 1:
            Ravenclaw += 1
        elif respuesta3 == 2:
            Hufflepuff += 1
        elif respuesta3 == 3:
            Gryffindor += 1
        elif respuesta3 == 4:
            Slytherin += 1
        else:
            print("No es una respuesta valida")
    print("¿Que camino te tienta más? \n 1.El carril amplio, soleado y cubierto de hierba \n 2.El callejón estrecho, oscuro e iluminado por linternas \n 3.El camino retorcido y cubierto de hojas a través del bosque \n 4.La calle adoquinada bordeada de edificios antiguos")
    respuesta4 = int(input("Escribe el numero de la respuesta: "))
    while respuesta4 not in range(1,4):
        if respuesta4 == 1:
            Hufflepuff += 1
        elif respuesta4 == 2:
            Slytherin += 1
        elif respuesta4 == 3:
            Ravenclaw += 1
        elif respuesta4 == 4:
            Gryffindor += 1
        else:
            print("No es una respuesta valida")
    print("Una vez cada siglo, el arbusto Flutterby produce flores que adaptan su aroma para atraer a los desprevenidos. Si te atrajera, olería a: \n 1.Una chimenea crepitante \n 2.Pergamino fresco \n 3.Tu hogar \n 4.El mar")
    respuesta5 = int(input("Escribe el numero de la respuesta: "))
    while respuesta5 not in range(1,4):
        if respuesta5 == 1:
            Gryffindor += 1
        elif respuesta5 == 2:
            Ravenclaw += 1
        elif respuesta5 == 3:
            Hufflepuff += 1
        elif respuesta5 == 4:
            Slytherin += 1
        else:
            print("No es una respuesta valida")
    #! Ahora mostraremos la casa con mas puntos.
    casas = {"Gryffindor":Gryffindor, "Hufflepuff":Hufflepuff, "Ravenclaw":Ravenclaw, "Slytherin":Slytherin}
    casa_seleccionada = max(casas, key=casas.get)
    print(" La casa seleccionada es: " + casa_seleccionada)
sombrero_seleccionador()
   