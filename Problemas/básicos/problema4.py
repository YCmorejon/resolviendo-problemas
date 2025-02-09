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


#Explicación sencilla paso a paso del código FizzBuzz

"""

1️-Definir la función 
   ```python
   def imprimir_fizz_buzz(inicio=1, fin=100):
   ```
   - Creamos la función `imprimir_fizz_buzz` con dos parámetros opcionales:  
     - `inicio`: indica desde qué número empieza el conteo (por defecto 1).  
     - `fin`: indica hasta qué número se cuenta (por defecto 100).  

---

2️-Recorrer los números en el rango
   ```python
   for num in range(inicio, fin + 1):
   ```
   - Usamos un bucle `for` para recorrer los números desde `inicio` hasta `fin` (incluyendo `fin`).  

---

3️-Verificar múltiplos de 3 y 5 (FizzBuzz) 
   ```python
   if num % 3 == 0 and num % 5 == 0:
       print("fizzbuzz")
   ```
   - Si el número es múltiplo de 3 y 5, imprimimos "fizzbuzz".  
   - Se verifica esta condición primero para evitar errores.

---

4️-Verificar múltiplos de 3 (Fizz)
   ```python
   elif num % 3 == 0:
       print("fizz")
   ```
   - Si solo es múltiplo de 3, imprimimos "fizz".  

---

5️-Verificar múltiplos de 5 (Buzz) 
   ```python
   elif num % 5 == 0:
       print("buzz")
   ```
   - Si solo es múltiplo de 5, imprimimos "buzz".  

---

6️-Si no es múltiplo de 3 ni de 5, imprimir el número
   ```python
   else:
       print(num)
   ```
   - Si no cumple ninguna condición anterior, simplemente imprimimos el número.

---

7-Ejecutar la función
   ```python
   imprimir_fizz_buzz()
   ```
   - Llamamos a la función sin parámetros, por lo que usará el rango de 1 a 100.

---

Resumen del comportamiento
- Números normales → se imprimen sin cambios.  
- Múltiplos de 3 → "fizz".  
- Múltiplos de 5 → "buzz".  
- Múltiplos de 3 y 5 → "fizzbuzz".  
"""

