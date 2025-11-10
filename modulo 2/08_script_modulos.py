import math
from math import sqrt

"""
En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas.
La importación de módulos nos permite acceder a
la funcionalidad definida en otros archivos y reutilizar código de manera eficiente. 
Además, podemos crear nuestros propios módulos para organizar y modularizar nuestro código.
"""


resultado = math.sqrt(25)
print("Raiz de 25:",resultado)  # Imprime 5.0

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print("Numero random entre 1-10: ",numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print("Fecha actual:",fecha_actual)  # Imprime la fecha y hora actual

import modulo

#llamado desde el modulo personalizado
modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8


resultado = modulo.sumar(5, 3)
modulo.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = modulo.obtener_nombre_usuario()
modulo.imprimir_mensaje(f"Hola, {nombre}!")

# Paquetes

# Crear y utilizar paquetes
"""
Para crear un paquete, creamos un directorio con el nombre deseado y
agregamos un archivo especial llamado __init__.py dentro del directorio. 
Este archivo puede estar vacío o contener código de inicialización del paquete.    
    
    """

from paquete1 import modulo2

modulo2.saludar("Fernando")  # Imprime "Hola, Fernando!"