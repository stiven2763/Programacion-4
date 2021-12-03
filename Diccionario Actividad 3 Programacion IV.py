# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:35:16 2021

"""

from pymongo import MongoClient

client= MongoClient("localhost")


db= client["Actividad3"]

basedatos = db['DiccionarioEspañol-Slang']



#La función que nos permitirá agregar nueva información
def agregar(var1,var2):
    
    basedatos.insert_one(({'Español':var1,
                        'Slang':var2}))
    
#La función que nos permitirá editar un información existente
def editar(var3,var4):
    basedatos.update_one({'Español': var3},
                         {"$set": {"Slang":var4}})

#La función que nos permitirá eliminar una fila existente
def eliminar(var5):
    basedatos.delete_many({'Español': var5})

#La función que nos permitirá imprimir la base de datos en pantalla
def verPalabras():
    for documentos in basedatos.find({}):
        print(documentos)
        
#La función que nos permitirá conocer el significa de una palabra
def Significado(var6): 
        for elementos in basedatos.find({'Español':var6}):
            print (elementos)

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
        var3 = input("Palabra en Español : ")
        var4 = input("Nuevo Significado : ")
        editar(var3,var4)

    BuscarSig = input("¿Quieres buscar el significado de una palabra ('Si' o 'No') : ")
    if BuscarSig == "Si":
        var6= input("Palabra en Español : ")
        Significado(var6)
        
    Imprimir = input("¿Quieres imprimir todo el diccionario ('Si' o 'No') : ")
    if Imprimir == "Si":
        verPalabras()
        
    Eliminar = input("¿Quieres eliminar una palabra del diccionario ('Si' o 'No') : ")
    if Eliminar == "Si":
        var5 = input("Palabra en Español a eliminar : ")
        eliminar(var5)
    
    Salir = input("¿Quieres salir del programa ('Si' o 'No') : ")
    if Salir == "Si":
        break
    
print("--------------------------------------------------")