from flask import Flask,render_template, request, redirect, url_for
import mysql.connector

app  = Flask(__name__)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwrod = "",
    database= "tiendita"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.rooute('/register', methods=['GET','POST'])
def registerTienda():
    if request.method == 'POST':
        id == request.form[id]
#        NombreMiselanea == request.form['NombreMiselanea']
        
        cursor = db.cursor
        cursor.excecute("INSERT INTO tienda (NombreMiselanea, Direccion, id_distribuidor) VALUES (%s, %s, %s)")