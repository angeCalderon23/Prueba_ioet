# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 23:00:31 2022

@author: ANGEL CAMILO
"""

# Variables

archivo = open("Prueba.txt","w")
Bandera = 0 # Enter and exit the schedules section
Bandera2 = 0 # Enter and exit the While

cont = 0
Otro = ""

BanderaH1 = 0
BanderaH2 = 0

Horario1 = False
Horario2 = False
Horario3 = False
Horario4 = False
Horario5 = False


# Lists
empleados = ["",]
horas = []
frecuencia = {}


#================================ Logic to implement ===============================

while Bandera2 == 0:
    
    
    empleado = input("Enter the name of the employees ")
    cont += 1
    empleados.append(empleado)
    archivo.write(empleado)
    igual = " = "
    archivo.write(igual)
            
        
    if empleado:
        print("Next you must enter the frequency of attendance of the employee containing hours and days\n")
        print("Enter as follows EJ : MO10:00-12:00 Where MO is Monday")
        Bandera = 1
        
    if Bandera == 1: 
        print("enter employee frequency")
        Horario1 = input("Enter first day and time ")
        archivo.write(Horario1)
                
    if (Horario1 or BanderaH1 == 1) and empleado:    
        Horario2 = input("enter second day and time ")
        archivo.write("," + Horario2) 
        
    if Horario2 == False and empleado:
        BanderaH2 = 1          
                
    if empleado: 
        Horario3 = input("enter third day and time ")
        archivo.write("," + Horario3)
        

    if empleado:
       Horario4 = input("enter fourth day and time ")
       archivo.write("," + Horario4)
       
    if empleado:
       Horario5 = input("enter fifth day and time ")
       archivo.write("," + Horario5 + "\n")
    
    print("\n")
    print ("Introduce another employee... Answer with the following syntax yes or no ")
    
    Otro = input("Answer ")
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
    print("The following shows the number of hours that are repeated among the employees: ")
    print("Example:'MO10:00-12:00': n where n is the number of times it is repeated\n")
    
    if cont >= 2: 
        for n in horas : 
            if n in frecuencia: 
                frecuencia[n] += 1 
            else: 
                frecuencia[n]=1
        empleados[cont]= empleados[cont]+ "-" + empleados[cont-1]
        print(empleados[cont] + " = " + str(frecuencia))
        

archivo.close()


        



        


