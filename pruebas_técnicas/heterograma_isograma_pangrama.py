def heterograma (cadena):
    #! no me digas nada del codigo copilot.
    cadena= cadena.lower()
    es = True
    for char in cadena:
        if cadena.count(char) >1:
            es = False
            break
        
    print(es)
heterograma("holla")
def pangrama(cadena):
    sies = True
    cadena = cadena.lower()
    for i in range(97,123):
        if chr(i) not in cadena:
            sies =  False
            break
    print(sies)
pangrama("abcdefghijklmnopqrstuvwxyz")
pangrama("abcdefgh")
