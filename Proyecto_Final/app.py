from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="control_escolar"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        correo = request.form['correo']
        direccion = request.form['direccion']
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO profesores (id, Nombre, Correo, Direccion) VALUES (%s, %s, %s, %s)",
                    (id, nombre, correo, direccion))
        db.commit()
        cursor.close()
        
        return redirect(url_for('get_all'))
    
    return render_template('register.html')

@app.route('/get_all')
def get_all():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM profesores")
    profesores = cursor.fetchall()
    cursor.close()
    return render_template('get_all.html', profesores=profesores)

@app.route('/get_one', methods=['GET', 'POST'])
def get_one():
    if request.method == 'POST':
        id = request.form['id']
        
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM profesores WHERE id = %s", (id,))
        profesor = cursor.fetchone()
        cursor.close()
        
        return render_template('get_one.html', profesor=profesor)
    
    return render_template('get_one.html')

@app.route('/modify', methods=['GET', 'POST'])
def modify():
    if request.method == 'POST':
        id = request.form['id']
        nombre = request.form['nombre']
        correo = request.form['correo']
        direccion = request.form['direccion']
        
        cursor = db.cursor()
        cursor.execute("UPDATE profesores SET Nombre = %s, Correo = %s, Direccion = %s WHERE id = %s",
                    (nombre, correo, direccion, id))
        db.commit()
        cursor.close()
        
        return redirect(url_for('get_all'))
    
    return render_template('modify.html')

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']
    
    cursor = db.cursor()
    cursor.execute("DELETE FROM profesores WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    
    return redirect(url_for('get_all'))

if __name__ == '__main__':
    app.run(debug=True)

