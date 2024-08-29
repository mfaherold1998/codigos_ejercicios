'''
* Crea un programa que sea capaz de transformar texto natural a código
* morse y viceversa.
* - Debe detectar automáticamente de qué tipo se trata y realizar
*   la conversión.
* - En morse se soporta raya "—", punto ".", un espacio " " entre letras
*   o símbolos y dos espacios entre palabras "  ".
* - El alfabeto morse soportado será el mostrado en
*   https://es.wikipedia.org/wiki/Código_morse.
''' 

import re
import sys

morse_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-',',': '--..--','?': '..--..','\'': '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-','@': '.--.-.', ' ': '/'
}

morse_dict_reverse = {v:k for k,v in morse_dict.items()}


def morse2txt(texto):
    words = texto.upper().split('  ')
    texto_txt = ''    
    for word in words:
        #word : '.... --- .-.. .-'
        for letra in word.split(' '):
            #letra: '....'
            texto_txt += morse_dict_reverse[letra]
        texto_txt += ' '
    #texto_morse: 'H O L A , '
    return texto_txt.strip()


def txt2morse(texto : str):
    words = texto.upper().split(' ')
    texto_morse = ''
    for word in words:
        #word : 'HOLA,'
        for letra in word:
            #letra: 'H'
            texto_morse += morse_dict[letra] + ' '
        texto_morse += ' '
    #texto_morse: 'H O L A , '
    return texto_morse.strip()

def funcion():
    
    if len(sys.argv) == 1 : 
        raise Exception('Pasa un texto como argumento, por favor coglione')
    
    texto = sys.argv[1]

    if re.search("[a-zA-Z0-9]",texto) :
        print(f'texto original: {texto}\ntexto morse: {txt2morse(texto)}') 
    else:
        print(f'texto original: {texto}\ntexto morse: {morse2txt(texto)}')

funcion()


    
