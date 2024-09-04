'''
* Escribe una función que calcule y retorne el factorial de un número dado
* de forma recursiva.
'''

def factorial( num: int ):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
print(factorial(5))