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

# Explicación 

"""
1-Lista de entrada:
Definimos una lista de números (lista) que será la entrada de nuestra función.

2-Definición de la función:
Creamos la función valor_maximo(lista) que toma como parámetro una lista de números.

3-Inicialización del valor máximo:
Usamos el primer elemento de la lista (lista[0]) como punto de partida para comparar.

4-Recorrido de la lista:
Iteramos sobre cada elemento de la lista:
-Si encontramos un número mayor que el actual valor almacenado en maximo, lo actualizamos.

5-Devolución del resultado:
Retornamos el valor máximo al final del bucle.

6-Mostrar el resultado:
Llamamos a la función con la lista de entrada y mostramos el número máximo con un mensaje claro.
"""
