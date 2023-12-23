import random

def dec2bin (valor):
    resultat = ""
    resReversed =""
    while valor >= 2:
        resultat = resultat + str(valor%2)
        valor = valor//2
    resultat = resultat + str(valor)
    for char in resultat:
        resReversed = char + resReversed
    return resReversed

def comprovaVotacio (strbin):
    cont =0
    for char in strbin:
        if char == '1':
            cont = cont + 1
    if cont > 2:
        return True
    else:
        return False


lst = ("dll","dm","dc","dj","dv")
acumLleisAprov =0
totalLleis = 0
for dia in (lst):        
    lleiaVotacio = random.randrange(1,10)
    resVotacio=""
    lleisAprovades= 0
    print ("número de lleis a votació: " + str(lleiaVotacio))
    for i in range(lleiaVotacio):
        votacio = random.randrange (0,31)
        print ("Resultat de la votació: " + str(votacio))
        resVotacio = dec2bin(votacio)
        if (comprovaVotacio(resVotacio)):
            print ("Llei aprovada " + resVotacio)
            lleisAprovades = lleisAprovades + 1
        else:
            print ("Llei no aprovada " + resVotacio)
    acumLleisAprov = acumLleisAprov + lleisAprovades
    totalLleis = totalLleis + lleiaVotacio
    print ("Lleis aprovades el " + dia +" "+  str(lleisAprovades))
    print ("-----------------------------------------")
if (acumLleisAprov < totalLleis/2):
    print (str(acumLleisAprov) + " Lleis aprovades de " + str(totalLleis) + " Regió ingovernable")
else:
    print (str(acumLleisAprov) + " Lleis aprovades de " + str(totalLleis) + " Regió controlada")