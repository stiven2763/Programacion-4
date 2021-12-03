import redis
r = redis.Redis(host="localhost",port="6379",db=0)
r.flushall()
#La función que nos permitirá agregar una nueva filas
def agregar(var1,var2):
    r.set(var1,var2)

#La función que nos permitirá editar una fila existente
def editar(var3,var4):
    r.delete(var3)
    r.set(var3,var4)

#La función que nos permitirá eliminar una fila existente
def eliminar(var5):
    r.delete(var5)

#La función que nos permitirá conocer el significa de una palabra
def Significado(var6):     
    significado = r.get(var6)
    print("El significado de la palabra ",var6, " es :", significado)

def verPalabras():
    valores = r.keys()
    for valor in valores:
        resultado = r.get(valor)
        print("La palabra : ",valor, "Significa en Slang : ", resultado)

print("Actividad N° 4 Diccionario Slang Panameño")

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
        var3 = input("Palabra en Español: ")
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
        var7 = input("Palabra en Español a eliminar : ")
        eliminar(var7)
    
    Salir = input("¿Quieres salir del programa ('Si' o 'No') : ")
    if Salir == "Si":
        break
    
print("--------------------------------------------------")