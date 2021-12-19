from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
import json


def application(environ,start_response):
    headers = [('Content-type','text/html')]
    start_response('200 OK', headers)

    response = {
        "payload ": "Hola mundo"
    }

    return [bytes(json.dumps(response),'utf-8')]

app = Flask(__name__)
#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'diccionarioslangpanameño'
mysql = MySQL(app)

#Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM palabras')
    data = cur.fetchall()
    return render_template('index.html',palabras = data)

@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method == 'POST':
        palabra = request.form['palabra']
        significado = request.form['significado']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO palabras(palabra,significado) VALUES(%s,%s)',(palabra,significado))
        mysql.connection.commit()
        flash('Palabra Añadida Correctamente')
        return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM palabras WHERE id = (%s)',(id))
    data = cur.fetchall()
    return render_template('edit-contact.html',palabras = data[0])

@app.route('/update/<string:id>',methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        palabra = request.form['palabra']
        significado = request.form['significado']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE palabras
            SET palabra = %s,
                significado = %s
            WHERE id = %s
            """,(palabra,significado,id))
        flash('Palabra actualizada satisfactoriamente')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM palabras WHERE id=(%s)',(id))
    mysql.connection.commit()
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 8000, debug = True)