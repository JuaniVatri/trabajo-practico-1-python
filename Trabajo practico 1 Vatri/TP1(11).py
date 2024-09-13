#Escribe una aplicación con una variable que contenga una contraseña cualquiera.
#Después se te pedirá que introduzcas la contraseña, con 3 intentos. Cuando aciertes ya
#no pedirá más la contraseña y mostrara un mensaje diciendo “Acceso Correcto”.
#Piensa bien en la condición de salida (3 intentos y si acierta sale, aunque le queden
#intentos). Si no acierta en ninguno de los 3 intentos, mostrar el mensaje “El acceso se
#ha bloqueado después de los 3 intentos”. Fin programa.


a=0
cont="pepe"
b="jajas"
for a in [1,2,3] or b==cont:
      b=input("ingresa la contraseña")
      if cont==b:
          print("Acceso correcto")
      a=a+1
print ("El acceso se bloqueó despues de tres intentos")  



     
