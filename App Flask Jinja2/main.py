from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
#Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'diccionario'
mysql = MySQL(app)

#Settings
app.secret_key = 'mysecretkey'


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM DiccionarioSlang')
    data = cur.fetchall()
    return render_template('index.html',DiccionarioSlang = data)

@app.route('/add_word',methods=['POST'])
def add_contact():
    if request.method == 'POST':
        Slang = request.form['Slang']
        Español = request.form['Español']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO DiccionarioSlang(Slang,Español) VALUES(%s,%s)',(Slang,Español))
        mysql.connection.commit()
        flash('La palabra ha sido agregada de forma correcta')
        return redirect(url_for('Index'))

@app.route('/edit/<string:id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM DiccionarioSlang WHERE id = (%s)',(id))
    data = cur.fetchall()
    return render_template('edit-palabra.html',DiccionarioSlang = data[0])

@app.route('/update/<string:id>',methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        Slang = request.form['Slang']
        Español = request.form['Español']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE DiccionarioSlang
            SET Slang = %s,
                Español = %s
            WHERE id = %s
            """,(Slang,Español,id))
        flash(':::Palabra actualizada:::')
        mysql.connection.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM DiccionarioSlang WHERE id=(%s)',(id))
    mysql.connection.commit()
    flash('La palabra ha sido eliminada de la base de datos')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 5000, debug = True)