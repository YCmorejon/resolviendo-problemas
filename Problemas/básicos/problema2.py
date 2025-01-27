# Ejercicio 2: Contar las ocurrencias de un número en una lista

"""
Enunciado:
Escribe una función que reciba una lista de números y un número objetivo, 
y que retorne cuántas veces aparece ese número en la lista.

Requisitos:
- La lista puede contener números enteros o decimales.
- La función debe retornar el número de ocurrencias del número objetivo en la lista.

Ejemplo de entrada y salida:
entrada = [1, 2, 3, 2, 4, 2]
objetivo = 2
salida = 3
"""

# Lista de entrada y número objetivo
entrada = [1, 2, 3, 4, 5, 6, "Hola", 3, 1.1, False, 3]
objetivo = 3

# Definición de la función
def contar_ocurrencias(lista, numero):
    """
    Esta función recibe una lista y un número objetivo.
    Retorna la cantidad de veces que aparece el número en la lista.
    
    Parámetros:
    - lista: la lista de elementos donde buscar.
    - numero: el número objetivo a contar.

    Retorno:
    - La cantidad de veces que el número aparece en la lista.
    """
    return lista.count(numero)

# Mostrar resultado
resultado = contar_ocurrencias(entrada, objetivo)
print(f"El número {objetivo} aparece {resultado} veces en la lista.")
