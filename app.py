from flask import Flask
from db import db
from flask import jsonify, request

from models.estudiante_model import Estudiante



db.connectToDb()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'CPLEX API'

@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    content_type = request.headers.get('Content-Type')
    estudiantes = [estudiante.serialize() for estudiante in db.view()]
    if (content_type == 'application/json'):
        json = request.json
        for estudiante in estudiantes:
            if estudiante['id'] == int(json['id']):
                return jsonify({
                    'res': estudiante,
                    'status': '200',
                    'msg': 'Success getting all estudiantes in library!👍😀'
                })
        return jsonify({
            'error': f"Error ⛔❌! Estudiante with id '{json['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    'res': estudiantes,
                    'status': '200',
                    'msg': 'Success getting all estudiantes in library!👍😀',
                    'no_of_estudiantes': len(estudiantes)
                })


@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    req_data = request.get_json()
    nombre = req_data['nombre']
    edad = req_data['edad']
    direccion = req_data['direccion']
    telefono = req_data['telefono']

    estudiantes = [estudiante.serialize() for estudiante in db.view()]
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:
            return jsonify({
                'res': f'Error ⛔❌! Estudiante with nombre {nombre} is already in library!',
                'status': '404'
            })

    estudiante = Estudiante(db.getNewId(), nombre, edad, direccion, telefono)
    print('new estudiante: ', estudiante.serialize())
    db.insert(estudiante)
    new_estudiantes = [estudiante.serialize() for estudiante in db.view()]
    print('estudiantes in lib: ', new_estudiantes)
    
    return jsonify({
                'res': estudiante.serialize(),
                'status': '200',
                'msg': 'Success creating a new estudiante!👍😀'
            })


if __name__ == '__main__':
    app.run(debug=True)