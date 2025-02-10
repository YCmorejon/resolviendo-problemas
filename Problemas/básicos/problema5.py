"""
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
 Un Anagrama consiste en formar una palabra reordenando TODAS
 las letras de otra palabra inicial.
 NO hace falta comprobar que ambas palabras existan.
 Dos palabras exactamente iguales no son anagrama.
 """

#Respuesta

# Anagramas
print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")



