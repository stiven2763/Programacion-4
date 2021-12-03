

#Importamos la librería sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import sessionmaker


#Establecemos la conexión con la base de datos Y creamos la base de datos

engine = create_engine("mariadb+mariadbconnector://root:1234@127.0.0.1:3307/actividad2")
Base=declarative_base()

#Creamos la tabla que almacenará los datos por medio de la clase DiccionarioSlangs

class DiccionarioSlangs(Base):

    __tablename__ = 'DiccionarioSlangs'
    Español = Column(String(100),primary_key=True)
    Slang = Column(String(100))

Session = sessionmaker(engine)
session= Session()
Base.metadata.create_all(engine)



# Definimos las funciones que nos permitirán manipular la base de datos
#La función que nos permitirá agregar una nueva filas
def agregar(var1,var2):
    Agregar = DiccionarioSlangs(Español=var1,Slang=var2)
    session.add(Agregar)
    session.commit()

#La función que nos permitirá editar una fila existente
def editar(var3,var4):
    Editar = session.query(DiccionarioSlangs).get(var3)
    Editar.Slang = var4
    session.commit()

#La función que nos permitirá eliminar una fila existente
def eliminar(var5):
    session.query(DiccionarioSlangs).filter(DiccionarioSlangs.Español == var5).delete()
    session.commit()


#La función que nos permitirá imprimir la base de datos en pantalla
def verPalabras():
    Palabras = session.query(DiccionarioSlangs).all()
    for Palabra in Palabras:
        print("Palabra Español es : " + Palabra.Español + " su significado es : " + Palabra.Slang)

#La función que nos permitirá conocer el significado de una palabra
def Significado(var6):     
    Significados = session.query(DiccionarioSlangs).filter_by(Español = var6)
    for Palabra in Significados:
        print("La palabra en español es : ",Palabra.Español,"; La palabra en Slang es : ",Palabra.Slang)


print("Actividad N° 2 Diccionario Slang Panameño Maria Db")

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
        var4= input("Palabra en Español : ")
        Significado(var4)
        
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