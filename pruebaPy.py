# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 23:00:31 2022

@author: ANGEL CAMILO
"""
 #Creacion TXT 


# Variables

archivo = open("Prueba.txt","w")
Bandera = 0 # Entra y sale de la seccion horarios
Bandera2 = 0 # Entrar y salir del While
Bandera3 = 0 # los espacios
cont = 0
Otro = ""
BanderaH1 = 0
BanderaH2 = 0
BanderaH3 = 0
BanderaH4 = 0
BanderaH5 = 0
Horario1 = False
Horario2 = False
Horario3 = False
Horario4 = False
Horario5 = False


# Listas
empleados = ["",]
horas = []
frecuencia = {}



#================================ Logica a efectuar ===============================

while Bandera2 == 0:
    
    
    empleado = input("Introduce nombre del empleado ")
    cont += 1
    empleados.append(empleado)
    archivo.write(empleado)
    igual = " = "
    archivo.write(igual)
            
        
    if empleado:
        print("A continuacion debe ingrezará la frecuencia de asistencia del empleado conteniendo horas y dias\n")
        print("Introduzca de la siguiente manera EJ : MO10:00-12:00 Donde MO es lunes")
        Bandera = 1
        
    if Bandera == 1: 
        print("ingrese frecuencia del empleado")
        Horario1 = input("Ingrese primer dia y hora ")
        archivo.write(Horario1)
                
    if (Horario1 or BanderaH1 == 1) and empleado:    
        Horario2 = input("ingrese segundo dia y hora ")
        archivo.write("," + Horario2) 
        
    if Horario2 == False and empleado:
        BanderaH2 = 1          
                
    if empleado: #Horario2 or Horario2 == False
        Horario3 = input("ingrese tercer dia  y hora ")
        archivo.write("," + Horario3)
        

    if empleado:
       Horario4 = input("ingrese cuarto dia y hora ")
       archivo.write("," + Horario4)
       
    if empleado:
       Horario5 = input("ingrese quinto dia y hora ")
       archivo.write("," + Horario5 + "\n")
    
    print("\n")
    print (" Introducira otro empleado? Responda con la siguiente sintaxis si o no ")
    
    Otro = input("Respuesta ")
    print("\n")

    if Otro == "no":
        Bandera2 = 1
    
    if cont >= 1:
        horas.append(Horario1)
        horas.append(Horario2)
        horas.append(Horario3)
        horas.append(Horario4)
        horas.append(Horario5)
        
    print(" \n")
    print("A continuacion se observara el numero de horas que se repiten entre los empleados: \n")
    
    if cont >= 2: 
        for n in horas : 
            if n in frecuencia: 
                frecuencia[n] += 1 
            else: 
                frecuencia[n]=1
                
        print(empleados[cont-1] + "-" + empleados[cont] + " = " + str(frecuencia))

archivo.close()



#empleados que se repiten

# print(" \n")
# print("A continuacion se observara el numero de horas que se repiten entre los empleados: \n")

# if cont >= 1: 
#     for n in horas : 
#         if n in frecuencia: 
#             frecuencia[n] += 1 
#         else: 
#             frecuencia[n]=1
            
#     print(empleados[cont-1] + "-" + empleados[cont] + " = " + str(frecuencia))


        



        


