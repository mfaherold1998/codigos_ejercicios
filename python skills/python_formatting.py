#F-string in python

name = 'Nanda'
age = 25
sentence = f'{name} is {age} years old.'
print(sentence)  # Output: Nanda is 25 years old.

num1 = 2
num2 = 3
sentence = f'La suma entre {num1} y {num2}es igual a {num1 + num2}'
print(sentence) #Output: La suma entre 2 y 3 es igual a 5

pi = 3.14159265359
sentence = f'El valor de pi es {pi:.2f}'
print(sentence) #Output: El valor de pi es 3.14

person ={
    'name': 'Nanda',
    'age': 25,
    'city': 'Bogota'
}
sentence = f'{person['name']} is {person["age"]} and is from {person['city']}'
print(sentence) #Output: Nanda is 25 and is from Bogota

text = 'Hello world'
sentence = f'The length of the text is {len(text)} characteres'
print(sentence) #Output: The length of the text is 11 characteres