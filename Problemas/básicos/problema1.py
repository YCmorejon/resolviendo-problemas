# Ejercicio 1: Sumar los números de una lista

"""
Enunciado:
Escribe una función que reciba una lista de números y devuelva la suma de todos los elementos de la lista.

Requisitos:
- La lista puede contener números enteros o decimales.
- La función debe retornar el valor de la suma.

Ejemplo de entrada y salida:
entrada = [1, 2, 3, 4, 5]
salida = 15
"""

# Lista de números
numeros = [2, 4, 6, 8]

# Definiendo la función
def sumar_lista(lista):
    """
    Esta función toma una lista de números y devuelve la suma de todos sus elementos.

    Parámetros:
    lista (list): Una lista de números (enteros o decimales).

    Retorna:
    int o float: La suma de los números en la lista.
    """
    return sum(lista)

# Mostrando el resultado
resultado = sumar_lista(numeros)
print(f"La suma de los números {numeros} es: {resultado}")  # Salida esperada: 20
