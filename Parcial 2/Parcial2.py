from flask import Flask,jsonify
import pandas as pd

#Iniciamos la aplicación en flask
app = Flask(__name__)

#Cargamos los datos del csv con la libreria pandas
df=pd.read_csv('Vacunas.csv')
#Convertimos los tipos de datos en Pandas
df = df.convert_dtypes()

#Creamos las rutas de lectura

#Mostramos todos los datos almacenados
@app.route('/Vacunas',methods=['GET'])
def Showalldata():
    Vacunas = df.dropna(1)
    Vacunas = Vacunas.to_json(orient='index')
    return jsonify(Vacunas)


#Filtramos los datos por paises
@app.route('/Vacunas/<string:Pais>',methods=['GET'])
def FiltroPaises(Pais):
    DataframeFinal = pd.DataFrame()
    DataframeFinal = df[df['Country Name']==Pais]
    DataframeFinal = DataframeFinal.dropna(1)
    Basedatos = DataframeFinal.to_json(orient='index')
    return jsonify(Basedatos)

@app.route('/Vacunas/<string:Pais>/<string:Year>',methods=['GET'])
def FiltroYear(Pais,Year):
    Datos_Filtrados = df[df['Country Name']==Pais]
    Datos_Filtrados  = Datos_Filtrados.dropna(1)
    Yearlist = Year.split(',')
    Datos_FiltradosAño  = Datos_Filtrados[Yearlist]
    DatosFinales = Datos_FiltradosAño.to_json(orient='index')
    return jsonify(DatosFinales)


app.run(debug=True,port=5000)