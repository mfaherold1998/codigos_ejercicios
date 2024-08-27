'''
Crear ambiente virtual

Implementar un algoritmo para generar constrasenas seguras
De modo que se pueda personalizar:
- La longitud de la contrasena
- Si incluir mayusculas o minusculas
- Si incluir numeros o caracteres especiales
- Cuantas constrasenas generar en la misma ejecucion
- Posibilidad de generar constrasennas a partir de una cadena o subcadena

Hacerle una interfaz grafica con Tkinter

url videos usados:
https://www.youtube.com/watch?v=TNtrAvNNxTY (entorno virtual)
https://www.youtube.com/watch?v=mYe-Ju8-D3o&list=PL_wRgp7nihybbJ2vZaVGI5TDdPaK_dFuC&index=82

'''

import random
from werkzeug.security import generate_password_hash

minus = 'abcdefghijklmnopqrstuvwxyz'
mayus = minus.upper()
numeros = '0123456789'
simbolos = '@[]{}*-/_+,;?!.$>#<%='

base = minus+mayus+numeros+simbolos
longitud = 12

for _ in range(10):
    muestra = random.sample(base,12)
    pasword = "".join(muestra)
    pasword_encriptada = generate_password_hash(pasword)
    print("{} => {}".format(pasword, pasword_encriptada))



















