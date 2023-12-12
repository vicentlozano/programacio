import random
"Primer farem un programa per pasar el número decimal a binari"
"Per a fer un programa utiitzem la fincio *def nom_del_programa(valor a introduir si fa falta):"
def deci2bin(valor):
    resultat = ""
    resultat_delrevés = ""
    while valor >= 2:
        resultat = resultat + str(valor % 2)
        valor = valor // 2
    resultat = resultat + str(valor)
    "Ara tenim que invertir els valors per a que ens done el resultat del binari"
    for char in resultat:
        resultat_delrevés = char + resultat_delrevés
    return resultat_delrevés
"val, una vegada tenim el programa per a convertir el decimal,continuem"
"el programa ha de generar un numero aleatori del 1 al 10 (random) que seran les lleis a tractar eixie dia"
"donat el número, ha de generar tants decimals  que transformats a binari tinguen 5 xifres com lleis s'ha de tractar"
"exemple, si es tramiten 3 lleis, haura de quedar algo com açò: 11111 10101 10001"
def comprovaVotacio (strbin) :
    cont = 0
    for char in strbin:
        if char == '1':
            cont = cont +1
        if cont > 2:
            return True
        else:
            return False
list= ("dilluns", "dimarts","dimecres","dijous","divendres")
acum_lleis_aprovades = 0
total_lleis = 0
for dia in (list):
    lleis_votacio = random.randrange(1,10)
    resVotacio=""
    lleisaprovades = 0
    print(" numero de lleis a votació: "+ str(lleis_votacio))
    for i in range(lleis_votacio):
        votacio = random.randrange(0,31)
        print("Resultat de la votació " + str(votacio))
        resVotacio = deci2bin(votacio)
        if (comprovaVotacio(resVotacio)):
            print("Lleis aprovada" + resVotacio)
            lleisaprovades = lleisaprovades + 1
        else:
            print("Llei no aprovada "+ resVotacio)
    acum_lleis_aprovades = acum_lleis_aprovades + lleisaprovades
    total_lleis = total_lleis + lleis_votacio
    print("Lleis aprovades el " + dia + " " + str(lleisaprovades))


if acum_lleis_aprovades<total_lleis/2:
    print(str(acum_lleis_aprovades) + "Lleis aprovades de " + str(total_lleis)+ " Regio ingovernable")
else:
    print ( str(acum_lleis_aprovades) + "Lleis aprovades de " + str(total_lleis) + "Regio controlada")

    
    


        


