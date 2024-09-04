'''
* Simula el funcionamiento de una máquina expendedora creando una operación
* que reciba dinero (array de monedas) y un número que indique la selección
* del producto.
* - El programa retornará el nombre del producto y un array con el dinero
*   de vuelta (con el menor número de monedas).
* - Si el dinero es insuficiente o el número de producto no existe,
*   deberá indicarse con un mensaje y retornar todas las monedas.
* - Si no hay dinero de vuelta, el array se retornará vacío.
* - Para que resulte más simple, trabajaremos en céntimos con monedas
*   de 5, 10, 50, 100 y 200.
* - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
'''

from typing import List
import os

class Machine:
    def __init__(self) -> None:
        self.consola = 'Maquina en funcionamiento\nSALDO: 00.00'
        self.dinero = {
            '5': 100, '10': 100, '20': 100, '50': 100, '100': 100, '200': 100
        }
        self.productos = {
            '1': {'nombre': 'Coca-Cola', 'precio': 150, 'cantidad': 0},
            '2': {'nombre': 'Fanta', 'precio': 120, 'cantidad': 5},
            '3': {'nombre': 'Sprite', 'precio': 100, 'cantidad': 5}
        }
        self.saldo = 200
        self.activa = True

    def set_consola(self, texto:str):
        self.consola = texto + '\n'

    def set_dinero(self, monedas:dict):
        self.dinero = monedas

    def set_productos(self, prod:dict):
        self.productos = prod

    def get_consola(self):
        return self.consola
    
    def get_saldo(self):
        return self.saldo
    
    def get_dinero(self):
        return self.dinero

    def get_productos(self):
        return self.productos
    
    def activar(self,flag=True):
        self.activa = flag
        if flag == True :
            self.consola = 'Maquina en funcionamiento\nSALDO: 00.00'
        else:
            self.consola = 'Maquina apagada'

    def dividir_saldo_en_monedas(self):
        #Lista de monedas de mayor a menor
        monedas = list(self.dinero.keys())[::-1]
        #Lista de tupla (moneda, cantidad)
        vuelto = []

        for mon in monedas:
            #Si el saldo no es 0
            if self.saldo > 0:
                #Cociente: cantidad de monedas a usar de ese valor para el vuelto
                #Resto: saldo restante
                cociente, resto = divmod(self.saldo,int(mon))
                #Si el cociente es 0 es porque esa moneda no se puede usar para el vuelto
                if cociente > 0:
                    vuelto.append((int(mon),cociente))#(moneda,cantidad)
                    self.saldo = resto
        
        return vuelto
    
    def dar_resto(self):
        #Recibir una lista de tuplas (moneda, cantidad)
        resto = []
        res = self.dividir_saldo_en_monedas()
        for moneda, cantidad in res:
            while cantidad != 0:
                resto.append(moneda)
                cantidad -= 1
        return resto
    
    def recibir_monedas(self, monedas):
        #Recibir una lista de monedas y convertir a centavos
        #for moneda in monedas:
        self.saldo = sum(monedas)#int(round(moneda * 100))

    def seleccion_producto(self, numero):
        #Comprobar que el numero de producto existe
        if numero in self.productos.keys():
            #Comprobar que el producto no esté agotado
            if self.productos[numero]['cantidad'] > 0:
                #Comprobar que el saldo es suficiente
                if self.saldo >= self.productos[numero]['precio']:
                    #Restar el precio del producto del saldo
                    self.saldo -= self.productos[numero]['precio']
                    #Restar 1 de la cantidad del producto
                    self.productos[numero]['cantidad'] -= 1
                else:
                    return 'saldo insuficiente'
            else:
                return 'agotado producto'
        else:
            return 'no existe'
        #Retorna el nombre del producto
        return self.productos[numero]['nombre'], self.saldo
    
def main():
    #Crear un objeto de la clase
    maquina_1 = Machine()
    #Menu de opciones
    
    while True :
        os.system('cls')
        saludo = int(input("""
                +--------------------------+
                |  Maquina Expendedora #1  |
    ---------------+---------------------+-------------------
    | Aqui tienes tus opciones:                               |
    | 1. Inserir monedas                                      |
    | 2. Seleccionar y recibir producto                       |
    | 3. Anular y recibir cambio                              |
    | 4. Salir                                                |
    ---------------------------------------------------------                                          
    """))
        if saludo not in ([1,2,3,4]):
            os.system('cls')
            print("Opción no válida, por favor elija una opción de la lista")
            input("Presione una tecla para continuar...")
        elif saludo == 1:
            os.system('cls')
            monedas = input('Inserte sus monedas en forma de lista separadas por comas con su valor en centavos: ')
            monedas = monedas.split(',')
            monedas = [int(moneda) for moneda in monedas]
            maquina_1.recibir_monedas(monedas)
            print(f'Su saldo es de {sum(monedas)}')
            input("Monedas recibidas")
        elif saludo == 2:
            os.system('cls')
            producto = input('Ingrese el número del producto que desea comprar: ')
            print(producto)
            prod, saldo = maquina_1.seleccion_producto(producto)
            print(f'producto: {prod} saldo: {saldo}')
            input("Presione una tecla para continuar...")
        elif saludo == 3:
            os.system('cls')
            print(f'Su cambio es: {maquina_1.dar_resto()}')
            input("Presione una tecla para continuar...")        
        elif saludo == 4:
            os.system('cls')
            print('Gracias por usar la maquina expendedora...')
            break

main()

