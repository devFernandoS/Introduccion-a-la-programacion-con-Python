#Funciones
"""
    Para definir una función en Python, 
    utilizamos la palabra clave def seguida del nombre de la función 
    y paréntesis. Opcionalmente, podemos especificar parámetros dentro de los paréntesis. 
    El bloque de código de la función se indenta después de los dos puntos.
"""
def saludo():   
    print("Hola a todos")

saludo() #Imprimer hola a todos    

#Funciones con parámetros
""" 
mismo metodo que la función anterior, pero ahora con un parámetro llamado nombre.
"""    
def saludo(nombre):
    print(f"¡Hola, {nombre}!")    

saludo("Fernando") #Imprime ¡Hola, Fernando!    

#Funciones con valor de retorno
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprime 7

# Funciones anonimas(ñambda)
"""
  Las funciones lambda en Python son funciones anónimas (sin nombre) que se definen en una sola línea.
  Son útiles para crear funciones pequeñas y temporales de forma rápida, especialmente cuando se 
  necesitan para ser usadas con otras funciones de orden superior como map(), filter() o sorted().
  Su sintaxis consiste en la palabra reservada lambda, seguida de los parámetros, 
  dos puntos y una única expresión cuyo resultado se retorna
 """
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25

# Una función lambda puede ser la entrada a una función normal.

def mi_funcion(lambda_func):
    return lambda_func(2,4)

mi_funcion(lambda a, b: a + b)

print(mi_funcion(lambda a, b: a + b))  # Imprime 6
print(mi_funcion(lambda a, b: a * b))  # Imprime 8

"""
    Documentación de funciones (docstrings)
Es una buena práctica documentar nuestras funciones utilizando docstrings. 
Los docstrings son cadenas de texto que describen el propósito, los parámetros y el valor de retorno de una función. 
Se colocan inmediatamente después de la definición de la función y se encierran entre triples comillas dobles.
    """
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura
    
"""
Funciones con número variable de argumentos
Python permite definir funciones que acepten un número variable de argumentos.
Esto se logra utilizando el operador * antes del nombre del parámetro.
"""

def suma_variable(*numeros):
    """
    suma una cantidad variable de números.

    Returns:
        total (float): La suma de los números proporcionados.
    """
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22