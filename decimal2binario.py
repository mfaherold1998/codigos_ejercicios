'''
* Crea un programa se encargue de transformar un número
* decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''

def dec2bin(num):
    bin = ''
    while (num//2 != 0):
        bin += str(num%2)
        num = num//2
    if num%2!= 0 : bin += str(num%2)
    bin = bin[::-1]
    return bin


def bin2dec(num): 
    num = num[::-1]
    dec = 0
    for i,j in enumerate(num):
        dec += int(j)*(2**i)
    return dec 


print(bin2dec('11010'))