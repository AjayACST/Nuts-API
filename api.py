import flask
from flask import jsonify
from flask import request
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



@app.route('/', methods=['GET'])
def home():
    return"<h1>RESTful Nut API</h1><p>This site is an API for providing images of nuts</p>"

@app.route('/v1/resources/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('nuts.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_nuts = cur.execute('SELECT * FROM nuts;').fetchall()

    return jsonify(all_nuts)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404



@app.route('/v1/resources', methods=['GET'])
def api_filter():
    query_params = request.args

    id = query_params.get('id')

    query = "SELECT * FROM nuts WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if not id:
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('nuts.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

