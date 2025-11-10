# Fundamentos de Python
"""
Tipos de datos básicos
    
- Números enteros (int): 
  Representan números enteros sin parte decimal. Ejemplo: 5, -3, 0

  edad = 30
  cantidad = 10

- Números de punto flotante (float): 
  Representan números con parte decimal. Ejemplo: 3.14, -0.001, 2.0
  
  precio = 19.99
  altura = 1.75

- Cadenas de texto (str): 
  Representan secuencias de caracteres. Se definen entre comillas simples (' ') o dobles (" "). Ejemplo: 'Hola', "Mundo"
  
  nombre = "fERNANDO"
  MENSAJE = 'Bienvenido a Python'
- Booleanos (bool): 
  Representan valores de verdad: True (verdadero) o False (falso).
  
  es_adulto = True
  tiene_permiso = False        
"""

nombre = "fERNANDO"
MENSAJE = 'Bienvenido a Python'
edad = 30  
es_adulto = True
print("Fundamentos de Python")
# string_formateado = f"{MENSAJE}, {nombre.capitalize()}" capitalize # Capitaliza la primera letra de la cadena

print(MENSAJE + ", " + nombre.capitalize()) # Concatenación de cadenas     
print("Usted tiene " + str(edad)+ " años.") # Conversión de entero a cadena para concatenar

altura=1.66
es_estudiante=True
#asignacion multiple
a = b = c = 10
print("Asignacion Multiple: a = b = c = 10")
print("Valor de a:", a)
print("Valor de b:", b)
print("Valor de c:", c)     

"""
#reservas invalidadas
1edad   # Comienza con un número
nombre-completo   # Utiliza un guion en lugar de un guion bajo
if   # Palabra clave reservada de Python
"""

#Aritméticos
a = 10
b = 3

suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
#  divide el primer valor por el segundo y devuelve un resultado de tipo entero (se descarta la parte decimal).
división_entera = a // b   # 3
# devuelve el resto de la división entre el primer valor y el segundo
modulo = a % b   # 1
# eleva el primer valor a la potencia del segundo.
exponenciacion = a ** b   # 1000

print()
print("Operadores Aritméticos:")
print("Valores de a y b:", a, b)
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division) # 3.3333333333333335 sin redondear
print("División Entera:", división_entera)
print("Módulo:", modulo)
print("Exponenciación:", exponenciacion)

# Operadores de comparación

igual = a == b   # False
diferente = a != b   # True
mayor_que = a > b   # True
menor_que = a < b   # False
mayor_o_igual = a >= b   # True
menor_o_igual = a <= b   # False
print()
print("Operadores de Comparación:") 
print("Valores de a y b:", a, b)
print("Igual:", igual)
print("Diferente:", diferente)
print("Mayor que:", mayor_que)  
print("Menor que:", menor_que)
print("Mayor o igual:", mayor_o_igual)

"""
Lógicos
AND (and): devuelve True si ambas condiciones son verdaderas.
OR (or): devuelve True si al menos una de las condiciones es verdadera.
NOT (not): invierte el valor de una condición, devuelve True si la condición es falsa y False si la condición es verdadera.

a = 10
b = 3

resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False

Python sigue las reglas de precedencia de operadores,
donde ciertos operadores tienen prioridad sobre otros.
En general, la precedencia sigue el orden: paréntesis, exponenciación, multiplicación/división, suma/resta,
operadores de comparación y operadores lógicos.
"""