# Ejercicio 5: Comprobar si dos palabras son anagramas

"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.

Un Anagrama consiste en formar una palabra reordenando TODAS las 
letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagramas.
"""

# Definiendo la función para comprobar anagramas
def comprobar_anagrama(palabra1, palabra2):
    # Si las palabras son idénticas, no son anagramas
    if palabra1.lower() == palabra2.lower():
        return False

    # Comparar las palabras ordenadas
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Probando con ejemplos
palabra1 = "hola"
palabra2 = "aloh"

resultado = comprobar_anagrama(palabra1, palabra2)
print(f"¿La palabra '{palabra1}' es anagrama de '{palabra2}'?: {resultado}")


#Explicacion 

"""
1️-Definir la función `comprobar_anagrama(palabra1, palabra2)` 
   - La función recibe dos palabras como parámetros y determinará si son anagramas.

2️-Verificar si las palabras son exactamente iguales  
   if palabra1.lower() == palabra2.lower():
       return False
   - Convertimos ambas palabras a minúsculas con `.lower()` para evitar que mayúsculas influyan.  
   - Si las palabras son idénticas, no son anagramas (porque no se reordenaron letras).  

3️-Ordenar y comparar las palabras
   return sorted(palabra1.lower()) == sorted(palabra2.lower())

   -`sorted(palabra.lower())` convierte la palabra en una lista de letras ordenadas alfabéticamente.  
   - Si ambas listas ordenadas son **idénticas**, significa que contienen las mismas letras en diferente orden.  

4️-Probar la función con un ejemplo
   palabra1 = "hola"
   palabra2 = "aloh"
   print(comprobar_anagrama(palabra1, palabra2))  # Salida: True
"""




