#Importamos la librería sqlalchemy
from enum import auto
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import INTEGER, Float, Integer, String
from sqlalchemy.orm import sessionmaker

#Establecemos la conexión con la base de datos Y creamos la base de datos

engine = create_engine("mariadb+mariadbconnector://root:1234@127.0.0.1:3307/parcial1")
Base=declarative_base()

#Creamos la tabla que almacenará los datos por medio de la clase Inventario

class Inventario(Base):

    __tablename__ = 'InventarioProducto'
    Producto = Column(String(100),primary_key=True)
    Cantidad = Column(Integer)
    Precio = Column(Float)
    Contratista = Column(String(100))


Session = sessionmaker(engine)
session= Session()
Base.metadata.create_all(engine)

# Definimos las funciones que nos permitirán manipular la base de datos
#La función que nos permitirá agregar una nueva filas
def agregar(var1,var2,var3,var4):
    Agregar = Inventario(Producto=var1,Cantidad=var2,Precio=var3,Contratista=var4)
    session.add(Agregar)
    session.commit()


 #La función que nos permitirá editar una fila existente
def editar(var5):
    Editar = session.query(Inventario).get(var5)
    pregunta= input("Deseas cambiar el precio de un producto ('Si' o 'No') :")
    if pregunta== "Si":
        var6 = float(input("Nuevo Precio : "))
        Editar.Precio = var6
    pregunta2= input("Deseas cambiar la cantidad de un producto ('Si' o 'No') :")
    if pregunta2 == "Si":
        var6 = int(input("Nueva Cantidad : "))
        Editar.Cantidad = var6
    else:
        var6 = (input("Nuevo Contratista : "))
        Editar.Contratista = var6
    session.commit()


#La función que nos permitirá eliminar una fila existente
def eliminar(var7):
    session.query(Inventario).filter(Inventario.Producto == var7).delete()
    session.commit()


#La función que nos permitirá imprimir la base de datos en pantalla
def verProductos():
    Productos = session.query(Inventario).all()
    for Productoss in Productos:
        print("Producto : " + Productoss.Producto + " Cantidad Disponible : " + str(Productoss.Cantidad)+ " Precio : " + str(Productoss.Precio) +
        " Contratista : " + Productoss.Contratista)

#La función que nos permitirá realizar una consulta
def Consultas(var8):     
    Consulta = session.query(Inventario).filter_by(Producto = var8)
    for Productoss in Consulta:
     print("Producto : " + Productoss.Producto + " Cantidad Disponible : " + str(Productoss.Cantidad) + " Precio : " + str(Productoss.Precio) +
        " Contratista : " + Productoss.Contratista)

print("Parcial N°1 Inventario en  Maria Db")

#Creamos un bucle while para iniciar el programa y que el usuario pueda interactuar

while True:
    Agregar = input("¿Quieres agregar un nuevo producto ('Si' o 'No') : ")
    if Agregar == "Si":
        flag = True
        while flag == True:
            var1=input("Producto : ")
            var2= int(input ("Cantidad : "))
            var3 = float(input ("Precio : "))
            var4 = input("Contratista :")
            agregar(var1,var2,var3,var4) #Llamamos a la función agregar que creamos previamente
            pregunta= input("¿Quieres añadir otra palabra? ('Si' o 'No') : ")
            if pregunta == "No":
                flag= False
    
    Editar= input("¿Quieres editar un producto ('Si' o 'No') : ")
    if Editar == "Si":
        var5 = input("Producto : ")
        editar(var5)

    BuscarP = input("¿Quieres buscar un producto('Si' o 'No') : ")
    if BuscarP == "Si":
        var8= input("Producto : ")
        Consultas(var8)
        
    Imprimir = input("¿Quieres imprimir todo el diccionario ('Si' o 'No') : ")
    if Imprimir == "Si":
        verProductos()
        
    Eliminar = input("¿Quieres eliminar una palabra del diccionario ('Si' o 'No') : ")
    if Eliminar == "Si":
        var7 = input("Palabra en Español a eliminar : ")
        eliminar(var7)
    
    Salir = input("¿Quieres salir del programa ('Si' o 'No') : ")
    if Salir == "Si":
        break
    
print("--------------------------------------------------")