'''
*Crear ambiente virtual

Implementar un algoritmo para generar constrasenas seguras
De modo que se pueda personalizar:
- La longitud de la contrasena
- Si incluir mayusculas o minusculas
- Si incluir numeros o caracteres especiales
- Cuantas constrasenas generar en la misma ejecucion
- Posibilidad de generar constrasennas a partir de una cadena o subcadena
- Posibilidad de guardar la contrasenna en un archivo

Controlar que la constrasena cumple con los requisitos de seguridad:
- Contiene al menos una mayuscula
- Contiene al menos una minuscula
- Contiene al menos un numero
- Contiene al menos un caracter especial

Hacer pruebas unitarias

Hacerle una interfaz grafica con Tkinter

url videos usados:
https://www.youtube.com/watch?v=TNtrAvNNxTY (entorno virtual)
https://www.youtube.com/watch?v=mYe-Ju8-D3o&list=PL_wRgp7nihybbJ2vZaVGI5TDdPaK_dFuC&index=82

'''

import random
from werkzeug.security import generate_password_hash
import os 

class Pasword:
    def __init__(self):
        self.body = ""

    def getText (self):
        return self.body
    
    def setText (self, texto):
        self.body = texto
    
    def getLength (self):
        return len(self.body)

class random_password_generator:
    def __init__(self, lenght=8, mayus=True, minus=True, numeros=True, simbolos=True):
        '''
        Clase para generar contraseñas aleatorias con opciones personalizables.

        Permite especificar la longitud de la contraseña y elegir si se incluyen 
        letras mayúsculas, letras minúsculas, números y/o símbolos especiales.
        '''
       
        self.base = ""
        self.longitud = lenght

        if minus : self.base += 'abcdefghijklmnopqrstuvwxyz'
        if mayus : self.base += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if numeros : self.base += '0123456789'
        if simbolos : self.base += '@[]{}*-/_+,;?!.$>#<%='

        
        

    def generate_random_pasword(self, cantidad=1):
        '''
        Genera una cantidad específica de contraseñas aleatorias según las especificaciones del constructor de la clase.

        Parámetros:
        n (int): El número de contraseñas a generar.

        Retorna:
        list: Una lista de contraseñas aleatorias con la longitud especificada.
        '''
        paswordsList = []
        for _ in range(cantidad):
            pasword = Pasword()
            muestra = random.sample(self.base, self.longitud)
            pasword.setText(pasword.getText().join(muestra))
            paswordsList.append(pasword)
        
        return paswordsList

    def encriptar_pasword(self, paswordsList):
        '''
        Encripta una lista de contraseñas y devuelve un diccionario con las contraseñas originales como claves 
        y sus versiones encriptadas como valores.

        Parámetros:
        passwords (list): Una lista de contraseñas a encriptar.

        Retorna:
        dict: Un diccionario en el formato {contraseña_original: contraseña_encriptada}.
        '''
        paswordEncriptadaList = {}
        for pasword in paswordsList:
            pasword_encriptada = generate_password_hash(pasword.getText())
            paswordEncriptadaList [pasword.getText()] = pasword_encriptada
        return paswordEncriptadaList
    
class random_secure_password_generator:
    def __init__(self):
        self.base = ''
        self.longitud = 0

        self.minus = 'abcdefghijklmnopqrstuvwxyz'
        self.mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numero = '0123456789'
        self.simbolo = '@[]{}*-/_+,;?!.$>#<%='
        self.base += self.minus+self.mayus+self.numero+self.simbolo



    def generate_secure_password(self, cantidad = 1):
        '''
        Genera una cantidad especificada de contraseñas que cumplen con los siguientes criterios:
        - Al menos un carácter en minúscula.
        - Al menos un carácter en mayúscula.
        - Al menos un carácter numérico.
        - Al menos un carácter simbólico.

        La longitud de cada contraseña se elige aleatoriamente.

        Parámetros:
        n (int): El número de contraseñas a generar.

        Retorna:
        list: Una lista de contraseñas que cumplen con los criterios especificados, cada una de longitud aleatoria.
        '''
        paswordsList = []
        for _ in range(cantidad):
            password = Pasword()
            self.longitud = random.randint(8,12)

            ranMinus = random.choice(self.minus)
            ranMayus = random.choice(self.mayus)
            ranNum = random.choice(self.numero)
            ranSim = random.choice(self.simbolo)

            temp = ranMinus+ranMayus+ranNum+ranSim

            while len(temp) < self.longitud :
                temp += random.choice(self.base)

            temp = list(temp)            
            random.shuffle(temp)                       
            password.setText(''.join(temp))
            paswordsList.append(password)

        return paswordsList
    
    def encriptar_pasword(self, paswordsList):
        '''
        Encripta una lista de contraseñas y devuelve un diccionario con las contraseñas originales como claves 
        y sus versiones encriptadas como valores.

        Parámetros:
        passwords (list): Una lista de contraseñas a encriptar.

        Retorna:
        dict: Un diccionario en el formato {contraseña_original: contraseña_encriptada}.
        '''
        paswordEncriptadaList = {}
        for pasword in paswordsList:
            pasword_encriptada = generate_password_hash(pasword.getText())
            paswordEncriptadaList [pasword.getText()] = pasword_encriptada
        return paswordEncriptadaList

class random_substring_generator_password:
    def __init__(self):
        
        self.base = ''
        self.longitud = 0

        self.minus = 'abcdefghijklmnopqrstuvwxyz'
        self.mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.numero = '0123456789'
        self.simbolo = '@[]{}*-/_+,;?!.$>#<%='
        self.base += self.minus+self.mayus+self.numero+self.simbolo

    def generate_password_substring (self, substring, cantidad = 1):
        '''
        Genera una cantidad especificada de contraseñas a partir de una cadena de caracteres proporcionada.

        Si la cadena contiene espacios, estos son eliminados automáticamente.
        La longitud de cada contraseña se elige aleatoriamente.

        Parámetros:
        n (int): El número de contraseñas a generar.

        Retorna:
        list: Una lista de contraseñas generadas a partir de la cadena dada, cada una de longitud aleatoria.
        '''
        paswordsList = []
        sub = substring.replace(" ", "")
        for _ in range(cantidad):
            password = Pasword()
            self.longitud = random.randint(8,12)
            sub = list(sub)
            random.shuffle(sub)
            sub = ''.join(sub)
            if len(sub) > self.longitud:
                sub = sub[:self.longitud]
            else:
                while len(sub) < self.longitud:
                    sub += random.choice(self.base)
            password.setText(sub)
            paswordsList.append(password)

        return paswordsList
    
    def generate_secure_password_substring (self, substring, cantidad = 1):
        '''
        Genera una cantidad especificada de contraseñas a partir de una cadena de caracteres dada,
        cumpliendo con los siguientes requisitos:

        - Cada contraseña contiene al menos un carácter en minúscula, un carácter en mayúscula,
        un carácter numérico y un carácter simbólico.
        - Estos caracteres obligatorios no se toman de la cadena proporcionada, sino que se 
        generan aleatoriamente en el código para asegurar su existencia.
        - Si la cadena contiene espacios, estos se eliminan automáticamente.
        - La longitud de cada contraseña se elige aleatoriamente.

        Parámetros:
        n (int): El número de contraseñas a generar.

        Retorna:
        list: Una lista de contraseñas generadas, cada una de longitud aleatoria.
        '''
        paswordsList = []
        sub = substring.replace(" ", "")
        for _ in range(cantidad):
            password = Pasword()
            self.longitud = random.randint(8,12)            
        
            if len(sub) > self.longitud:
                sub += random.choice(self.mayus)
                sub += random.choice(self.minus)
                sub += random.choice(self.numero)
                sub += random.choice(self.simbolo)
                sub = sub[-(self.longitud) : ]
                sub = list(sub)
                random.shuffle(sub)
                sub = ''.join(sub)
            else:
                sub += random.choice(self.mayus)
                sub += random.choice(self.minus)
                sub += random.choice(self.numero)
                sub += random.choice(self.simbolo)
                while len(sub) < self.longitud:
                    sub += random.choice(self.base)
                sub = sub[-(self.longitud) : ]
                sub = list(sub)
                random.shuffle(sub)
                sub = ''.join(sub)               

                    
            password.setText(sub)
            paswordsList.append(password)
    
        return paswordsList
    
    def encriptar_pasword(self, paswordsList):
        '''
        Encripta una lista de contraseñas y devuelve un diccionario con las contraseñas originales como claves 
        y sus versiones encriptadas como valores.

        Parámetros:
        passwords (list): Una lista de contraseñas a encriptar.

        Retorna:
        dict: Un diccionario en el formato {contraseña_original: contraseña_encriptada}.
        '''
        paswordEncriptadaList = {}
        for pasword in paswordsList:
            pasword_encriptada = generate_password_hash(pasword.getText())
            paswordEncriptadaList [pasword.getText()] = pasword_encriptada
        return paswordEncriptadaList



while True :
    os.system('cls')
    saludo = int(input("""
                +---------------------+
                |   Ready Player One  |
 ---------------+---------------------+-------------------
| Aqui tienes tus opciones para generar contraseñas:      |
| 1. Generar contraseñas aleatorias.                      |
| 2. Generar contraseñas seguras aleatorias               |
| 3. Generar contraseñas aleatorias a partir de una frase |
| 4. Leer documentacion de los generadores                |
| 5. Salir                                                |
 ---------------------------------------------------------                                          
"""))
    if saludo not in ([1,2,3,4,5]):
        print("Opción no válida, por favor elija una opción válida")
        input()
    elif saludo == 1 :
        os.system('cls')
        res = input("""Con este generador puedes crear una o varias contraseñas aleatorias de 8 caracteres entre los que se incluyen letras en mayuscula, minuscula, numeros y simbolos. Desea crear contraseñas con estas caracteristicas?(yes/no): _
""")
        if res.lower() == 'yes':
            cantidad = input('Indique la cantidad de contraseñas a generar: _')
            generator = random_password_generator()
            passwords = generator.generate_random_pasword(int(cantidad))
            print ('Sus contraseñas son: ')
            for p in passwords:
                print(p.getText())
            input('Desea guardarlas en un fichero a parte?(yes/no):_')
            if res.lower() == 'yes':
                name = input('Indique el nombre del fichero: _')
                encriptadas = generator.encriptar_pasword(passwords)
                with open(name + '.txt', 'w') as f:
                    for p in encriptadas.keys():
                        f.write('password: {} => {}\n'.format(p,encriptadas[p]))
            input('Todas las contraseñas se han guardado en su version original y encriptadas...')
            
        else:
            longitud = input('Indique la longitud de las contraseñas a generar: _')
            minus = input('Inclir letras minusculas? (yes/no): _')
            if minus == 'no':
                minus = False
            else:
                minus = True
            mayus = input('Incluir letras mayusculas? (yes/no): _')
            if mayus == 'no':
                mayus = False
            else:
                mayus = True
            numeros = input('Incluir numeros? (yes/no): _')
            if numeros == 'no':
                numeros = False
            else:
                numeros = True            
            simbolos = input('Incluir simbolos? (yes/no): _')
            if simbolos == 'no':
                simbolos = False
            else:
                simbolos = True
            cantidad = input('Indique la cantidad de contraseñas a generar: _')
            generator = random_password_generator(int(longitud), mayus, minus, numeros, simbolos)
            passwords = generator.generate_random_pasword(int(cantidad))
            print ('Sus contraseñas son: ')
            for p in passwords:
                print(p.getText())
            input('Desea guardarlas en un fichero a parte?(yes/no):_')
            if res.lower() == 'yes':
                name = input('Indique el nombre del fichero: _')
                encriptadas = generator.encriptar_pasword(passwords)
                with open(name + '.txt', 'w') as f:
                    for p in encriptadas.keys():
                        f.write('password: {} => {}\n'.format(p,encriptadas[p]))
            input('Todas las contraseñas se han guardado en su version original y encriptadas...')


    elif saludo == 2:
        pass
    elif saludo == 3:
        pass
    elif saludo == 4:
        pass
    elif saludo == 5:
        os.system('cls')
        print("""
                +---------------------+
                | Goodbye Player One  |
                +---------------------+
                """)
        break
    
    



















