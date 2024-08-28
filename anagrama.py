'''
* Escribe una función que reciba dos palabras (String) y retorne
* verdadero o falso (Bool) según sean o no anagramas.
* - Un Anagrama consiste en formar una palabra reordenando TODAS
*   las letras de otra palabra inicial.
* - NO hace falta comprobar que ambas palabras existan.
* - Dos palabras exactamente iguales no son anagrama.
'''

def check_anagrama (word1, word2):
    if word1.lower() == word2.lower():
        return False
    else:
        return set(word1.lower()).issubset(set(word2.lower()))
    
res = input('Escriba dos palabras separadas por comas: ')
word1, word2 = res.split(',')
print( f'{word1} y {word2} son anagramas: { check_anagrama(word1, word2)}') # True o False