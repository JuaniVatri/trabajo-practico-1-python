#Lee un número por teclado e indica si es divisible entre 2 (resto = 0). Si no lo es,
#también debemos indicarlo.
num= float(input ("Introduce un numero: "))
if num % 2==0:
    print (num, " es divisible por dos")
else:
    print (num, " no es divisible por dos")