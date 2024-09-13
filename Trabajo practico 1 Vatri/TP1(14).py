#Codifique un programa de consola en Python que permita realizar las siguientes acciones:
#Generar un número aleatorio entre 0 y 100, para ello use la siguiente función:
#random.randint(0, 100)
#Una vez generado el número codifique la lógica necesaria para encontrar el número aleatorio 
# ayudando al usuario informando al mismo si el número ingresado es mayor o menor al número 
# aleatorio buscado. Una vez encontrado el número muestre la cantidad de intentos necesarios para lograrlo.
#Ejemplo: Número aleatorio generado: 63
#Ingrese un número entre 0 y 100.
#Numero Ingresado: 50
#Respuesta: Es muy bajo
#Ingrese un número entre 0 y 100.
#Numero Ingresado: 75
#Respuesta: Es muy alto
#Ingrese un número entre 0 y 100.
#Numero Ingresado: 60
#Respuesta: Es muy bajo
#Ingrese un número entre 0 y 100.
#Numero Ingresado: 65
#Respuesta: Es muy alto
#Ingrese un número entre 0 y 100.
#Numero Ingresado: 63
#Respuesta: Correcto, numero encontrado, cantidad de intentos 5
import random
na=random.randint(0,100)
nu=int(input("Ingrese un numero entre 0 y 100"))
cont=0
while na!=nu:
    if na>nu :
        print ("Es muy bajo")
        nu=int(input("Ingrese un numero entre 0 y 100"))
    if na<nu:
        print ("Es muy alto")
        nu=int(input("Ingrese un numero entre 0 y 100"))
    cont+=1
if nu==na:
    print(f"Encontró el número, que es {na}, numero de intentos {cont}")

