"""
    Error de sintaxis (SyntaxError)
Ocurre cuando el código no sigue las reglas de sintaxis de Python, como olvidar dos puntos después de una declaración de función o un bucle.
def mi_funcion() # Falta los dos puntos
    print("Hola")
    """
    
"""
Error de nombre (NameError)
Ocurre cuando se hace referencia a una variable o función que no ha sido definida.

print(variable_no_definida)
"""    

"""
Error de tipo (TypeError)
Ocurre cuando se realiza una operación con tipos de datos incompatibles, como intentar sumar un número y una cadena.
resultado = 5 + "10"
"""

"""
Error de índice (IndexError)
Ocurre cuando se intenta acceder a un índice fuera del rango válido de una lista o secuencia.
lista = [1, 2, 3]
print(lista[3])  # El índice 3 está fuera del rango
"""
#Try
"""
El bloque try contiene el código que puede generar una excepción. 
Si ocurre una excepción dentro del bloque try, 
el flujo de ejecución se transfiere al bloque except correspondiente.
"""
try:
    #codigo que puede generar una excepxion
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero no está permitida.")    

#Except
"""
El bloque except especifica el tipo de excepción que se desea capturar y manejar. 
Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.
"""

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")
    
#Finally
"""
El bloque finally es opcional y se ejecuta siempre, independientemente de
si ocurrió una excepción o no.
Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos.
"""
archivo = None
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
except NameError:
    print("Error: Nombre de variable 'archivo' no definido")    #No evita el error del finally
finally:
    if archivo:
       archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción

#Traceback (most recent call last):
#  File "c:\Users\willian\Desktop\Cursos\Python Santander\modulo 2\06_script_errores_excepciones.py", line 67, in <module>
#    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción
#    ^^^^^^^
#NameError: name 'archivo' is not defined
    
# Excepciones personalizadas

"""
    
Para crear una excepción personalizada, 
debes crear una clase que herede de la clase base Exception o de una de sus subclases.    
"""
edad=-1
def funcion():
    # Código que puede generar una excepción personalizada
    if edad<0:
        raise Exception("Descripción del error")

try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")
"""
En este ejemplo, se define una función llamada funcion(). Dentro de la función, 
se verifica una condición y, si se cumple, se genera una excepción utilizando la declaración raise.
En lugar de crear una clase personalizada, 
se utiliza directamente la clase base Exception para generar la excepción.
"""    