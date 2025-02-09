# El famoso "FizzBuzz"

"""
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def imprimir_fizz_buzz(inicio=1, fin=100):
    """
    Imprime los números del rango dado, reemplazando:
    - "fizzbuzz" en múltiplos de 3 y 5.
    - "fizz" en múltiplos de 3.
    - "buzz" en múltiplos de 5.
    
    Parámetros:
    - inicio (int): Número inicial del rango (incluido).
    - fin (int): Número final del rango (incluido).
    """
    for num in range(inicio, fin + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

# Mostrando resultados
imprimir_fizz_buzz()
