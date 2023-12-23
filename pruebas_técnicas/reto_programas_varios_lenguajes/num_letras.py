print("Este programa te permite contar las letras de una palabra o una oración.")
escrito = str(input("Escribe lo que quieras: "))
letra = str(input("Que letra quieres contar?: "))
def contador_letras(letra,escrito):
    count = 0
    for char in escrito:
        if char == letra: count +=1
    return count
print(contador_letras(letra,escrito))
