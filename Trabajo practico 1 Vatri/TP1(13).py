#Pide un número por teclado e indica si es un número primo o no.
#Un número primo es aquel solo puede dividirse entre 1 y sí mismo. Por ejemplo: 25 no es primo, 
#ya que 25 es divisible entre 5, sin embargo, 17 si es primo. Un buen truco para calcular la raíz cuadrada del 
#numero e ir comprobando que si es divisible desde 
#ese número hasta 1. NOTA: Si se introduce un número menor o igual que 1, directamente es no primo.
import math
i=0
n= int(input("Ingrese un numero: "))
variaR= math.sqrt(n)
if variaR - int(variaR)==0:
    print("No es numero primo")
else:
    while n % (int(variaR)-i)!=0 :
     i+=1
    if n % (int(variaR)-i)==0 and i!=int(variaR)-1:
       print("No es primo")
    else:
       print("Es primo")
