# estructura Condicionales
edad = 18

print("Estructuras de Control - Condicionales")

if edad >= 18:
    print("Eres mayor de edad.")
print()

if edad>= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")        

"""
   IF-ELIF-ELSE
La estructura if-elif-else nos permite especificar múltiples condiciones y bloques de código alternativos. La sintaxis básica es la siguiente:

if condicion1:

   # Bloque de código a ejecutar si la condicion1 es verdadera
   instrucciones

elif condicion2:

   # Bloque de código a ejecutar si la condicion2 es verdadera
   instrucciones

else:

   # Bloque de código a ejecutar si ninguna condición anterior es verdadera
   instrucciones 
"""   

calificacion = 85

print()
print("Estructura if-elif-else")    
print("Calificación:", calificacion)

if calificacion >= 90:
   print ("Excelente")

elif calificacion >= 80:
   print ("Muy bueno")

elif calificacion >= 70:
   print ("Bueno")

else:
   print ("Necesita mejorar")
   
#bubles y loops
"""
 Estructura For
for variable in secuencia:
    
    # Bloque de código a repetir
    instrucciones
"""    
print()
print("Estructura For")
for i in range(3):
    print("Iteración:", i)

frutas=["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Fruta:", fruta)    
   
"""
 Estructura While
while condicion:
    
    # Bloque de código a repetir
    instrucciones
"""
print()
print("Estructura While")
print("Contador de 0 a 2:")
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1   
        
        
# Control de bucles

"""
 Control de bucles 
Break
La instrucción break se utiliza para salir prematuramente de un bucle,
independientemente de la condición. Cuando se encuentra un break, 
el bucle se detiene y el flujo de ejecución continúa con la
siguiente instrucción fuera del bucle.

Continue
La instrucción continue se utiliza para saltar el resto del bloque de
código dentro de un bucle y pasar a la siguiente iteración.

Pass
La instrucción pass es una operación nula que no hace nada. 
cuando se requiere una instrucción sintácticamente, 
pero no se desea realizar ninguna acción.
"""   

contador = 0

print()
print("Uso de Break en While cuando contador llega a 5:")
while True:
#inicio while
    print(contador)
    contador += 1

    if contador == 5:
        break
#finalizacion while            
    
print()
print("Uso de Continue en For para saltar números pares:")    
for i in range(10):
    
    if i % 2 == 0:
        continue
    print(i)
    
for i in range(5):
    pass  #error/problem: Either remove or fill this block of code.

"""
En este ejemplo, el bucle for itera sobre los números del 0 al 4, 
pero no se realiza ninguna acción dentro del bucle debido a la instrucción pass. 
Esto puede ser útil cuando se está desarrollando
un programa y se desea reservar un bloque de 
código para implementarlo más adelante.    
"""
    