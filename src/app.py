import json
import sqlite3
import pandas as pd
from flask import Flask, render_template, jsonify
import os
from os.path import dirname, join


app = Flask(__name__, static_url_path='', static_folder='./static')
db_name = 'data.db'
db_path = join(dirname(dirname(__file__)), db_name)


@app.route("/api/get_data")
def get_data():
    sql_conn = sqlite3.connect(db_path)
    df = pd.read_sql('select entity, value from parsed_data', sql_conn)
    data = df.to_dict(orient='list')
    return jsonify(data)


@app.route("/")
def display():
    return render_template('display.html')


if __name__ == "__main__":
    app.run()