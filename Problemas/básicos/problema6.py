#Ejercicio 1: Suma de los primeros N números

"""
Enunciado: Escribe un programa en Python que calcule la suma de los primeros N números naturales (empezando desde 1). La variable N debe ser proporcionada por el usuario.
Ejemplo: Si el usuario ingresa 5, la salida será 1 + 2 + 3 + 4 + 5 = 15.
"""


#Respuesta

# Solicitar la variable del usuario
while True:
    try:
        N = int(input("¿Cuál es tu variable? "))
        break
    except ValueError:
        print("Introduce un valor válido, debe ser un número entero.")

# Definir función para calcular el valor
def calcular(n):
    suma = 0
    while n > 0:
        suma += n
        n -= 1
    return suma

# Mostrar el resultado
resultado = calcular(N)
print(f"El resultado es: {resultado}")

#Explicacion
