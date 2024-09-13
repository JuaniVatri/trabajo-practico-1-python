
#Criterios de divisibilidad del 2
#Para saber si un número es divisible entre dos hay que comprobar que sea par
divdos=False
num=int(input("Ingrese un numerito: "))
if num % 2==0:
       print(f"{num} es par, divisible por dos")
       divdos=True
else:
       print(f"{num} no es par, no es divisible por dos")


#Criterios de divisibilidad del 3
#Sumamos las cifras del número y si el resultado de la suma es un número múltiplo de 3,
#  entonces el número sí es divisible por 3.
#numero = int(input("Digite un numero que desee que se sume sus digitos: "))
numcad= str(num)
suma = 0
divtres=False
for i in numcad:
        suma += int(i)
suma= int(suma)
if suma%3==0:
    print (f"{num} es divisible por 3")
    divtres=True 
else:
    print (f"{num} no es divisible por 3")

#Criterio de divisibilidad del 5
#Para saber si un número es divisible entre 5, dicho número tiene que acabar en 0 o 5
if numcad[-1] =="0" or numcad[-1] =="5":
    print(f"{num} es divisible por 5")
else:
    print(f"{num} no es divisible por 5")

#Criterios de divisibilidad del 6
#Si se cumplen los criterios del 2 y del 3, entonces también es divisible por 6
if divdos==True and divtres==True:
    print (f"{num} es divisible por 6")
else:
    print(f"{num} no es divisible por 6")

#Criterio de divisibilidad del 9
#Un número es divisible entre 9 cuando la suma de sus dígitos es 9 o múltiplo de 9.
#Por ejemplo, vamos a comprobar si 2610 es un múltiplo de 9.
#2 + 6 + 1 + 0 = 9, por lo tanto 2610 es divisible por 9.
if suma%9==0:
    print (f"{num} es divisible por 9")
     
else:
    print (f"{num} no es divisible por 9")


if numcad[-1] =="0":
    print(f"{num} es divisible por 10")
else:
    print(f"{num} no es divisible por 10")


