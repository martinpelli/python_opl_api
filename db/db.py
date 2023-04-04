import random
import sqlite3
from models.estudiante_model import Estudiante

estudiantes = [
    {
        'nombre': 'pelli',
        'edad': 23,
        'direccion': 'los cedros',
        'telefono':  '26412345'
    },
    {
        'nombre': 'lucho',
        'edad': 24,
        'direccion': 'av. cordoba',
        'telefono':  '264123453'
    }
]    

def connectToDb():
    conn = sqlite3.connect('estudiantes.db')
    print("Connection to database successfully")

    query = "SELECT name FROM sqlite_master WHERE type='table' AND name='estudiantes'"

    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Table already exists")
    else:
        conn.execute('CREATE TABLE estudiantes (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER, direccion TEXT, telefono TEXT)')
        print("Estudiantes table created successfully")
        for i in estudiantes:
            estudiante = Estudiante(getNewId(), i['nombre'], i['edad'], i['direccion'], i['telefono'])
            insert(estudiante)

    conn.close()

def getNewId():
    return random.getrandbits(28)

def insert(estudiante : Estudiante):
    conn = sqlite3.connect('estudiantes.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO estudiantes VALUES (?,?,?,?,?)", (
        estudiante.id,
        estudiante.nombre,
        estudiante.edad,
        estudiante.direccion,
        estudiante.telefono
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('estudiantes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM estudiantes")
    rows = cur.fetchall()
    estudiantes = []
    for i in rows:
        estudiante = Estudiante(i[0], True if i[1] == 1 else False, i[2], i[3], i[4])
        estudiantes.append(estudiante)
    conn.close()
    return estudiantes

def updateById(estudiante : Estudiante):
    conn = sqlite3.connect('estudiantes.db')
    cur = conn.cursor()
    cur.execute("UPDATE estudiantes SET nombre=?, edad=?, direccion=?, telefono=? WHERE id=?", (estudiante.nombre, estudiante.edad, estudiante.direccion, estudiante.telefono))
    conn.commit()
    conn.close()

def deleteById(id):
    conn = sqlite3.connect('estudiantes.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM estudiantes WHERE id=?", (id))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('estudiantes.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM estudiantes")
    conn.commit()
    conn.close()

