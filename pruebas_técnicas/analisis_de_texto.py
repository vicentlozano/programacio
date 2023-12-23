"""
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 """
import statistics
texto_a_analizar  = str(input("Escribe el texto a analizar: "))
def numero_palabras_i_lista_palabras(texto_a_analizar):
   palabras =  texto_a_analizar.split()
   numero_de_palabras = int(len(palabras))
   return numero_de_palabras,palabras
def encontrar_palabra_larga_i_longitudes(palabras):
   longitudes = []
   for i in range(len(palabras)):
    palabras[i] = palabras[i].replace(".", "")
         
   for i in palabras:
      
      longitudes.append(len(i))
   longitud_mayor = max(longitudes)
   indice_palabra_larga = longitudes.index(longitud_mayor)
   media = statistics.mean(longitudes)

   return palabras[indice_palabra_larga],media
def contar_numero_oraciones(texto_a_analizar):
   numero_oraciones = texto_a_analizar.count(".")
   return numero_oraciones
numero_palabras, palabras = numero_palabras_i_lista_palabras(texto_a_analizar)
palabra_larga,media = encontrar_palabra_larga_i_longitudes(palabras)
numero_oraciones  = contar_numero_oraciones(texto_a_analizar)
print("Número total de palabras: " + str(numero_palabras)+ ". La palabra más larga es: "+ palabra_larga + ". La Longitud media de las palabras es: " + str(media) + ". Número de oraciones del texto (cada vez que aparecen un punto,palabra más larga) es: " + str(numero_oraciones))

     
   


