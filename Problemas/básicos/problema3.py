# Ejercicio 3: Encontrar el número máximo en una lista

"""
Enunciado:
Escribe una función que reciba una lista de números y devuelva el número más grande de la lista.

Requisitos:
- La lista puede contener números enteros o decimales.  
- La función debe retornar el valor del número máximo.  
- No se permite usar la función `max()` de Python.  

Ejemplo de entrada y salida:
Entrada:  
numeros = [3, 1, 9, 2, 5]

Salida:  
9
"""
#Respuesta 

# Lista de números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Función para encontrar el valor máximo
def valor_maximo(lista):
    maximo = lista[0]  # Inicializamos con el primer elemento de la lista
    for numero in lista:
        if numero > maximo:  # Si encontramos un número mayor, lo actualizamos
            maximo = numero
    return maximo

# Mostrando el resultado
resultado = valor_maximo(lista)
print(f"El valor máximo de la lista es: {resultado}")
