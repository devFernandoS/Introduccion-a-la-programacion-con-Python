#Entrada de datos del usuario

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")


print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")

edad = int(input("Ingresa tu edad: "))# Convertir la entrada a un entero


if edad >= 18: #evitar error de tipo
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    
    
nombre = "Fernando"
edad = 25

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")    
#En este caso, las variables se incrustan dentro de la cadena utilizando llaves {} y
# se precede la cadena con la letra f para indicar que es una f-string.

#Lectura y escritura de archivos 
"""
Python nos permite leer y escribir datos en archivos externos. Podemos abrir archivos en diferentes modos,
como lectura ("r"), escritura ("w") o anexar ("a"),
y realizar operaciones de lectura y escritura.
    
    """
#Lectura de archivos
##Usa el path de la terminaral para leer el archivo.
archivo = open( "datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()    

#Escritura de archivos
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

"""
En este ejemplo, se abre el archivo "datos.txt" en modo de escritura utilizando open().
Luego, se escribe la cadena 
"¡Hola, mundo!" en el archivo utilizando el método write(). Finalmente, 
se cierra el archivo utilizando el método close()        
"""

with open("datos2.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)    #Imprime el contenido del archivo linea a linea
    
"""
En este caso, el archivo se abre utilizando la declaración with y se cierra automáticamente una 
vez que se sale del bloque with, incluso si ocurre una excepción.
"""    