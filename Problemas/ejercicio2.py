#Ejercicio 2: Contar las ocurrencias de un número en una lista

""""
Enunciado:

Escribe una función que reciba una lista de números y un número objetivo, y que retorne cuántas veces aparece ese número en la lista.

Requisitos:
- La lista puede contener números enteros o decimales.
- La función debe retornar el número de ocurrencias del número objetivo en la lista.

Ejemplo de entrada y salida:
entrada = [1, 2, 3, 2, 4, 2]
objetivo = 2
salida = 3
"""

#Respuesta

#Entrada y objetivo
entrada = [1,2,3,4,5,6,"Hola",3,1.1,False,3]
objetivo = 3

#Creando Función
def Buscar(entrada,objetivo):
    return entrada.count(objetivo)

#Mostrando Resultado
print(Buscar(entrada,objetivo))
