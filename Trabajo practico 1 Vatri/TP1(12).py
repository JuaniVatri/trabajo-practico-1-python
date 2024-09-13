#Crea una aplicación que nos pida un día de la semana y que nos diga si es un dia
#laboral o no (siendo sábado y domingo no laborales). Usa un switch para ello. Valida
#que el número ingresado sea un valor entre 1 y 7, caso contrario solicite el valor
#nuevamente. Debe investigar cuales son las alternativas que se pueden codificar para
#reemplazar o emular una estructura switch por ejemplo implementando diccionarios.
#Dado que Python no posee esta estructura por defecto.
dia=-1
while 1> dia or dia >7:
    dia= int(input("Ingrese un numero de día de la semana: "))      
if dia== 1 or dia==2 or dia==3 or dia==4 or dia==5:
       print ("Es un dia laboral")
else:
 if dia== 6 or dia==7:
       print ("Es un dia no laboral")
#fin   
