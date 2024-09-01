'''
* Crea una función que reciba dos cadenas como parámetro (str1, str2)
* e imprima otras dos cadenas como salida (out1, out2).
* - out1 contendrá todos los caracteres presentes en la str1 pero NO
*   estén presentes en str2.
* - out2 contendrá todos los caracteres presentes en la str2 pero NO
*   estén presentes en str1.
'''

def strDiff (cad1:str, cad2:str):
    out1 = set(cad1).difference(set(cad2))
    out2 = set(cad2).difference(set(cad1))
    return out1, out2

print(strDiff('abcdefg','defghijk'))