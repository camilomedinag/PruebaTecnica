from maximo_cuadrado import maximo_cuadrado
from maximo_rectangulo import maximo_rectangulo
from iterador_celdas_libres import iterador_celdas_libres
import json
from flask import Flask, request, Response, jsonify, g
import sqlite3
DATABASE = 'medinaDB.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def add_name(new_ans):
    query = "INSERT INTO Answer (ans) VALUES (?);"
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute(query, [str(new_ans)])
    cursor.close()
    connection.commit()
    
def listar_todo():
    query = "SELECT * FROM Answer"

    connection = get_db()
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    
    return results

@app.route('/maximo_rectangulo', methods=['POST'])
def maximo_rectangulo_solver():
    matrix = request.data.decode("utf-8") 
    matrix = [[int(x) for x in y.split()] for y in matrix.split("\n")]
    answer = maximo_rectangulo(matrix) 
    add_name(answer)
    return jsonify([int(x) for x in answer])

@app.route('/maximo_cuadrado', methods=['POST'])
def maximo_cuadrado_solver():
    matrix = request.data.decode("utf-8") 
    matrix = [[int(x) for x in y.split()] for y in matrix.split("\n")]
    answer = maximo_cuadrado(matrix)
    add_name(answer)
    return jsonify([int(x) for x in answer])

@app.route('/iterador_celdas_libres', methods=['POST'])
def celdas_libres():
    matrix = request.data.decode("utf-8") 
    [i, j] = [int(x) for x in matrix.split("\n")[0].split()]
    matrix = [[int(x) for x in y.split()] for y in matrix.split("\n")[1:]]
    answer = iterador_celdas_libres(matrix,i,j)
    add_name(answer)
    if(answer):
        return jsonify([list(x) for x in answer])
    return jsonify([False])

@app.route('/respuestas', methods=['GET'])
def listar_respuestas():
    for i in listar_todo():
        print(i[0])
    return jsonify([x[0] for x in listar_todo()])
