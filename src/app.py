import json
import sqlite3
import pandas as pd
from flask import Flask, render_template
import os
from os.path import dirname, join


app = Flask(__name__, static_url_path='', static_folder='./static')
db_name = 'data.db'
db_path = join(dirname(dirname(__file__)), db_name)


@app.route("/")
def display_data():
    sql_conn = sqlite3.connect(db_path)
    df = pd.read_sql('select entity, value from parsed_data', sql_conn)
    data = df.to_dict(orient='list')
    data = json.dumps(data)
    return render_template('display.html', data=data)


if __name__ == "__main__":
    app.run()