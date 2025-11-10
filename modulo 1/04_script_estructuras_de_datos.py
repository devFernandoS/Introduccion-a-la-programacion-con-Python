# Estructuras de datos
""" Listas en Python:
"""
mi_lista = [1, 2, 3, 4, 5]
print("Lista:", mi_lista)   
frutas=["manzana", "banana", "cereza"]
print("Frutas:", frutas)
print("Primer fruta:", frutas[0])  # Acceder al primer elemento
# Acceder desde el final de la lista
print("Última fruta:", frutas[-1])  # Acceder al último elemento
print("penultimo fruta",frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

#Métodos de listas
"""
    Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista.
    Algunos métodos comunes son:

append(elemento): agrega un elemento al final de la lista.
insert(indice, elemento): inserta un elemento en una posición específica de la lista.
remove(elemento): elimina la primera aparición de un elemento en la lista.
pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
sort(): ordena los elementos de la lista en orden ascendente.
reverse(): invierte el orden de los elementos en la lista.
"""
print("\n")
print("Métodos de listas:")
frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

# Listas de comprensión
"""
Las listas de comprensión
son una forma concisa de crear nuevas listas basadas en una secuencia existente. 
Permiten filtrar y 
transformar los elementos de una lista en una sola línea de código.

nueva_lista = [expresion for elemento in secuencia if condicion]

"""

numeros = [1, 2, 3, 4, 5]
cubos = [x ** 3 for x in numeros if x % 2 == 0]
print("\n")
print("Listas de comprensión: Cubo de numeros pares")
print("Números:", numeros)  # Imprime [1, 2, 3, 4, 5]
print(cubos)  # Imprime [16, 64]

# Tuplas en Python:
"""
Una tupla es una estructura de datos inmutable y
ordenada que permite almacenar una colección de elementos. 
Los elementos de una tupla se encierran entre paréntesis (),
separados por comas.
"""

punto = (3, 4)
# Para acceder a los elementos de una tupla, 
# utiliza el índice del elemento entre corchetes,
# similar a las listas:
print("\n")
print("Tuplas:")
print("punto[0]",punto[0])  # Imprime 3
print("punto[1]",punto[1])  # Impirme 4

# A diferencia de las listas,
# las tuplas son inmutables, lo que significa que no se pueden modificar 
# una vez creadas.
# No se pueden agregar, eliminar o cambiar elementos en una tupla existente.

# Las tuplas son útiles cuando necesitas almacenar una colección de elementos que no deben modificarse, 
# como coordenadas o datos de configuración.

""" 
    Métodos de tuplas
Aunque las tuplas son inmutables, Python proporciona varios métodos útiles para trabajar con ellas:

count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. 
Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve 
la longitud de la tupla.
"""

mi_tupla = (1, 2, 3, 2, 4, 2)
print ("_Busqueda en tupla\n")
print("mi tupla",mi_tupla)
print ("mi tupla.index(2):",mi_tupla.index(2))   # Salida: 1
print ("mi_tupla.index(2, 2)->> , busca el 2 desde el subindexe 2")
print (mi_tupla.index(2, 2))   #Salida: 3
print ("mi_tupla.index(2, 2, 4)->> , busca el 2 desde el subindexe 2 hasta el 4")
print (mi_tupla.index(2, 2, 4))   #Salida: 3


# Diccionarios en Python:
"""
Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor.
Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. Los diccionarios se encierran entre llaves {}, 
y los pares clave-valor se separan por comas.
"""    
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Argentina"}
print(persona["nombre"])  # Imprime "Juan"
print(persona["edad"])    # Imprime 25
print(persona["ciudad"])  # Imprime "Madrid"

# También puedes utilizar el método get() 
# para obtener el valor de una clave. Si la clave no existe,
# devuelve un valor predeterminado (por defecto, None).
print(persona.get("nombre"))  # Imprime "Juan"
print(persona.get("profesion", "Desconocida"))  # Imprime valor default:"Desconocida"

"""
    Métodos de diccionarios
Los diccionarios en Python tienen varios métodos incorporados para manipular y 
acceder a los elementos. Algunos métodos comunes son:

keys(): devuelve una vista de todas las claves del diccionario.
values(): devuelve una vista de todos los valores del diccionario.
items(): devuelve una vista de todos los pares clave-valor del diccionario.
update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
"""
print("\n")
print("Métodos de diccionarios:")
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Argentina"}


print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Argentina"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Argentina")])


persona.update({"profesion": "Ingeniero"})
print("Agregando clave-valor, profesion-Ingeniero")
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Argentina", "profesion": "Ingeniero"}

# Conjuntos (set) en Python:


""""
Un conjunto es una estructura de datos mutable 
y no ordenada que permite almacenar una colección de elementos únicos.
Los conjuntos se encierran entre llaves {} o se crean utilizando la función set().
"""

print("\n")
print("Conjuntos:")

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])# Replace this set constructor call by a set literal.

# Los conjuntos admiten operaciones matemáticas de conjuntos, como la unión (|), 
# la intersección (&), la diferencia (-) y la diferencia simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2#inverso de intersepcion
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}


# Métodos de conjuntos
"""
# Los conjuntos en Python tienen varios métodos 
# incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

# add(elemento): agrega un elemento al conjunto.
# remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
# discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
# clear(): elimina todos los elementos del conjunto.

"""
frutas = {"manzana", "banana", "naranja"}


frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()