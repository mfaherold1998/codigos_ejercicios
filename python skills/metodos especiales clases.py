'''
En Python, los **métodos especiales** (también llamados *dunder methods* porque comienzan y terminan con dobles guiones bajos, como `__method__`) son funciones integradas en las clases que permiten modificar el comportamiento de las instancias de esas clases en operaciones estándar. Estos métodos te permiten sobrecargar operadores, hacer que los objetos sean iterables, gestionar el contexto con `with`, entre otros.

Aquí te dejo una lista lo más completa posible de los métodos especiales en Python, clasificados por funcionalidad:

### Métodos de inicialización y destrucción
- **`__init__(self, ...)`**: Inicializa una nueva instancia de la clase.
- **`__new__(cls, ...)`**: Controla la creación de una nueva instancia de la clase.
- **`__del__(self)`**: Destructor; se llama cuando el objeto está a punto de ser destruido.

### Representación y conversión a cadenas
- **`__str__(self)`**: Devuelve una representación en formato de cadena del objeto (usado por `str()` y `print()`).
- **`__repr__(self)`**: Devuelve una representación formal de la instancia (usado por `repr()`, útil para depuración).
- **`__format__(self, format_spec)`**: Define cómo se debe formatear el objeto (usado por `format()`).
- **`__bytes__(self)`**: Convierte el objeto a una cadena de bytes (usado por `bytes()`).
- **`__hash__(self)`**: Devuelve el valor hash del objeto (usado por `hash()`).

### Conversión de tipos
- **`__bool__(self)`**: Define la conversión a `bool` (usado por `bool()`).
- **`__int__(self)`**: Define la conversión a `int` (usado por `int()`).
- **`__float__(self)`**: Define la conversión a `float` (usado por `float()`).
- **`__complex__(self)`**: Define la conversión a `complex`.
- **`__index__(self)`**: Define cómo el objeto se convierte a un índice entero (usado por operadores como `[]`).
- **`__len__(self)`**: Devuelve el tamaño del objeto (usado por `len()`).

### Comparación y ordenación
- **`__eq__(self, other)`**: Define la igualdad (`==`).
- **`__ne__(self, other)`**: Define la desigualdad (`!=`).
- **`__lt__(self, other)`**: Define el menor que (`<`).
- **`__le__(self, other)`**: Define el menor o igual que (`<=`).
- **`__gt__(self, other)`**: Define el mayor que (`>`).
- **`__ge__(self, other)`**: Define el mayor o igual que (`>=`).

### Operadores aritméticos
- **`__add__(self, other)`**: Suma (`+`).
- **`__sub__(self, other)`**: Resta (`-`).
- **`__mul__(self, other)`**: Multiplicación (`*`).
- **`__matmul__(self, other)`**: Multiplicación de matrices (`@`).
- **`__truediv__(self, other)`**: División real (`/`).
- **`__floordiv__(self, other)`**: División entera (`//`).
- **`__mod__(self, other)`**: Módulo (`%`).
- **`__pow__(self, other)`**: Potencia (`**`).
- **`__and__(self, other)`**: AND bit a bit (`&`).
- **`__or__(self, other)`**: OR bit a bit (`|`).
- **`__xor__(self, other)`**: XOR bit a bit (`^`).
- **`__lshift__(self, other)`**: Desplazamiento a la izquierda (`<<`).
- **`__rshift__(self, other)`**: Desplazamiento a la derecha (`>>`).

### Operadores aritméticos reflejados (cuando el operando izquierdo no soporta la operación)
- **`__radd__(self, other)`**: Suma reflejada.
- **`__rsub__(self, other)`**: Resta reflejada.
- **`__rmul__(self, other)`**: Multiplicación reflejada.
- **`__rmatmul__(self, other)`**: Multiplicación de matrices reflejada.
- **`__rtruediv__(self, other)`**: División real reflejada.
- **`__rfloordiv__(self, other)`**: División entera reflejada.
- **`__rmod__(self, other)`**: Módulo reflejado.
- **`__rpow__(self, other)`**: Potencia reflejada.

### Operadores aritméticos en versión "in-place"
- **`__iadd__(self, other)`**: Suma en el lugar (`+=`).
- **`__isub__(self, other)`**: Resta en el lugar (`-=`).
- **`__imul__(self, other)`**: Multiplicación en el lugar (`*=`).
- **`__imatmul__(self, other)`**: Multiplicación de matrices en el lugar (`@=`).
- **`__itruediv__(self, other)`**: División real en el lugar (`/=`).
- **`__ifloordiv__(self, other)`**: División entera en el lugar (`//=`).
- **`__imod__(self, other)`**: Módulo en el lugar (`%=`).
- **`__ipow__(self, other)`**: Potencia en el lugar (`**=`).
- **`__iand__(self, other)`**: AND bit a bit en el lugar (`&=`).
- **`__ior__(self, other)`**: OR bit a bit en el lugar (`|=`).
- **`__ixor__(self, other)`**: XOR bit a bit en el lugar (`^=`).
- **`__ilshift__(self, other)`**: Desplazamiento a la izquierda en el lugar (`<<=`).
- **`__irshift__(self, other)`**: Desplazamiento a la derecha en el lugar (`>>=`).

### Operadores de contenedores e índices
- **`__getitem__(self, key)`**: Sobrecarga para acceder a un elemento (`obj[key]`).
- **`__setitem__(self, key, value)`**: Sobrecarga para asignar un valor (`obj[key] = value`).
- **`__delitem__(self, key)`**: Sobrecarga para eliminar un elemento (`del obj[key]`).
- **`__contains__(self, item)`**: Define si un elemento está en el contenedor (`item in obj`).

### Iteración
- **`__iter__(self)`**: Devuelve un iterador (usado en bucles `for`).
- **`__next__(self)`**: Devuelve el siguiente elemento del iterador.
- **`__reversed__(self)`**: Devuelve un iterador para recorrer el objeto en orden inverso.
- **`__len__(self)`**: Devuelve la longitud del objeto (usado por `len()`).

### Gestión de contexto (usado por `with`)
- **`__enter__(self)`**: Definido al entrar en un bloque de contexto (usado por `with`).
- **`__exit__(self, exc_type, exc_value, traceback)`**: Definido al salir de un bloque de contexto.

### Atributos y propiedades
- **`__getattr__(self, name)`**: Se llama cuando se accede a un atributo que no existe.
- **`__getattribute__(self, name)`**: Se llama para acceder a cualquier atributo (existe o no).
- **`__setattr__(self, name, value)`**: Se llama cuando se asigna un valor a un atributo.
- **`__delattr__(self, name)`**: Se llama cuando se elimina un atributo.
- **`__dir__(self)`**: Devuelve una lista de atributos del objeto (usado por `dir()`).

### Gestión de memoria
- **`__sizeof__(self)`**: Devuelve el tamaño en bytes del objeto (usado por `sys.getsizeof()`).

### Llamable y callable
- **`__call__(self, ...)`**: Sobrecarga la llamada de un objeto como si fuera una función.

### Comparación de identidad
- **`__instancecheck__(self, instance)`**: Define cómo `isinstance()` debe comportarse con el objeto.
- **`__subclasscheck__(self, subclass)`**: Define cómo `issubclass()` debe comportarse.

### Otros
- **`__copy__(self)`**: Define cómo copiar el objeto (`copy.copy()`).
- **`__deepcopy__(self, memo)`**: Define cómo realizar una copia profunda del objeto (`copy.deepcopy()`).

Estos métodos especiales permiten controlar y personalizar muchos aspectos del comportamiento de los objetos en Python, lo que hace que el lenguaje sea extremadamente flexible y poderoso.
'''