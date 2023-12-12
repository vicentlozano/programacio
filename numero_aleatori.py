import random
num_aleatori = random.randint(1,100)
intents  = int(input("cuants intents vols tindre per endevinar el número?"))
cont = 0
while cont<intents:
    resposta = int(input("Disme el número: "))
    if resposta == num_aleatori:
        print ("Has encertat!")
        break
    else:
        print("No es aquest número.")
        cont += 1
        if resposta < num_aleatori:
            print("No, es menor.El rang está entre ")