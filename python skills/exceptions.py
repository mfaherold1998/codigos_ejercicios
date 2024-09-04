#Exceptions: Errors detected during execution
'''
mensajes de error => tipo:the built-in exception that occurred

ejemplo: TypeError: TypeError: can only concatenate str (not "int") to str
'''

#Ejemplo 1
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except (RuntimeError, TypeError, NameError):
        print("Oops!  That was no valid number.  Try again...")

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)

'''
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
'''
import sys

#Else statement
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

#Raising exceptions
#The raise statement allows the programmer to force a specified exception to occur.
raise NameError('HiThere')
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere'''

#If an exception class is passed, it will be implicitly instantiated 
# by calling its constructor with no arguments:
raise ValueError  # shorthand for 'raise ValueError()'

#determine whether an exception was raised but don’t intend to handle it
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

#Common exceptions: https://docs.python.org/3/library/exceptions.html#base-classes