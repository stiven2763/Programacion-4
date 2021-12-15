
## Importamos las librerias que utilizaremos
from flask import Flask,jsonify,request
from basedato import verPalabras,Significado,agregar,editar,eliminar
app = Flask(__name__)


#Creamos las rutas
@app.route('/Diccionario')
def obtenerpalabras():
    Palabras = verPalabras()
    return jsonify(Palabras)

@app.route('/Diccionario/<string:Espanol>')
def get(Espanol):
      Palabra = Significado(Espanol)
      print(Palabra)
      if Palabra!=None and Palabra != []:
          return jsonify(Palabra)
      else:
          return jsonify({"message":'Palabra No encontrada'})

@app.route('/Diccionario',methods=['POST'])
def addpalabra():
    var1=request.json['Espanol']
    var2= request.json["Slang"]
    agregar(var1,var2)
    Palabra = verPalabras()
    return jsonify({'message ':'Palabra añadida correctamente',"Palabras":Palabra})

@app.route('/Diccionario/<string:Espanol>',methods =['PUT'])
def editsignificado(Espanol):
    Palabra = verPalabras()
    if Palabra !=None and Palabra != []:
        var3 = request.json['Espanol']
        var4= request.json['Slang']
        editar(var3,var4)
        return jsonify({"message":'Palabra Modificada Correctamente'})
    else:
        return jsonify({"message":'Palabra No encontrada'})

@app.route('/Diccionario/<string:Espanol>',methods=['DELETE'])
def deleteProduct(Espanol):
    Palabra = verPalabras()
    if Palabra !=None and Palabra != []:
        var5 = request.json['Espanol']
        eliminar(var5)
        Palabra = verPalabras()
        return jsonify({"message":'Palabra Eliminada Correctamente',"Palabras":Palabra})
    else:
        return jsonify({"message":'Palabra No encontrada'})

if __name__ == '__main__':
    app.run(debug=True,port=5000)