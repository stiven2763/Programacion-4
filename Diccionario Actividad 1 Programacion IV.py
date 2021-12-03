# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:43:18 2021

"""


#Importamos la librería sqlite3 para trabajar con las bases de datos


import sqlite3

#Establecemos la conexión con la base de datos Y creamos la base de datos

conexion = sqlite3.connect('Actividad1.db')


cursor = conexion.cursor()

#Creamos la tabla que almacenará los datos

cursor.execute("""CREATE TABLE if not exists DiccionarioSlang (
            ID integer primary key AUTOINCREMENT,Slang text,
            Español text
            )""")

conexion.commit()  #Esta linea de código guardar los cambios realizados


# Definimos las funciones que nos permitirán manipular la base de datos


#La función que nos permitirá agregar una nueva filas
def agregar(var1,var2):
    cursor.execute("insert into DiccionarioSlang(Slang,Español) VALUES (?,?)", (var1,var2))
    conexion.commit()

#La función que nos permitirá editar una fila existente
def editar(var3,var4):
    cursor.execute("UPDATE DiccionarioSlang SET Español = '%s' WHERE Slang ='%s'" % (var4,var3))
    conexion.commit()

#La función que nos permitirá eliminar una fila existente
def eliminar(var3):
    cursor.execute("delete from DiccionarioSlang WHERE Español= '%s'" % var3)
    conexion.commit()
    
#La función que nos permitirá imprimir la base de datos en pantalla
def verPalabras():
    cursor.execute("SELECT Id, Slang, Español from DiccionarioSlang")
    filas = cursor.fetchall()
    for fila in filas:
        print("\nSlang= ", fila[1], "Significado Español = ", fila[2])
        
#La función que nos permitirá conocer el significa de una palabra
def Significado(var4):     
    cursor.execute("select Slang, Español from DiccionarioSlang WHERE Español = '%s'" % var4)
    filas = cursor.fetchall()
    for fila in filas:
        print("El significado de la palabra", fila[0],"es : ", fila[1])

print("Actividad N° 1 Diccionario Slang Panameño")

#Creamos un bucle while para iniciar el programa y que el usuario pueda interactuar

while True:
    Agregar = input("¿Quieres agregar una nueva palabra ('Si' o 'No') : ")
    if Agregar == "Si":
        flag = True
        while flag == True:
            var1=input("Palabra : ")
            var2= input ("Significado : ")
            agregar(var1,var2) #Llamamos a la función agregar que creamos previamente
            pregunta= input("¿Quieres añadir otra palabra? ('Si' o 'No') : ")
            if pregunta == "No":
                flag= False
    
    Editar= input("¿Quieres editar una palabra ('Si' o 'No') : ")
    if Editar == "Si":
        var3 = input("Palabra en Slang : ")
        var4 = input("Nuevo Significado : ")
        editar(var3,var4)

    BuscarSig = input("¿Quieres buscar el significado de una palabra ('Si' o 'No') : ")
    if BuscarSig == "Si":
        var4= input("Palabra en Español : ")
        Significado(var4)
        
    Imprimir = input("¿Quieres imprimir todo el diccionario ('Si' o 'No') : ")
    if Imprimir == "Si":
        verPalabras()
        
    Eliminar = input("¿Quieres eliminar una palabra del diccionario ('Si' o 'No') : ")
    if Eliminar == "Si":
        var3 = input("Palabra en Español a eliminar : ")
        eliminar(var3)
    
    Salir = input("¿Quieres salir del programa ('Si' o 'No') : ")
    if Salir == "Si":
        break
    
print("--------------------------------------------------")
conexion.close()
