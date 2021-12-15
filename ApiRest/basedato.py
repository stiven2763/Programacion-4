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
    palabras = []
    for documentos in basedatos.find({}):
        dicc = {}
        dicc['Espanol'] = documentos['Español']
        dicc['Slang'] = documentos['Slang']
        palabras.append(dicc)
    return palabras
        
#La función que nos permitirá conocer el significa de una palabra
def Significado(var6): 
    palabra=[]
    for elementos in basedatos.find({'Español':var6}):
        dicc = {}
        dicc['Espanol'] = elementos['Español']
        dicc['Slang'] = elementos['Slang']
        palabra.append(dicc)
    return palabra
