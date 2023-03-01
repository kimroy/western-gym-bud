from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import psycopg2
from data import helper_functions as helper

app = Flask(__name__)

conn = psycopg2.connect(
    host='db',
    database=helper.get_env_var('POSTGRES_DB'),
    user=helper.get_env_var('POSTGRES_USER'),
    password=helper.get_env_var('POSTGRES_PASSWORD')
)
cur = conn.cursor()

@app.route('/')
def index():
    return redirect(url_for('table'))
    # return render_template('index.html')

@app.route('/table', methods=['POST', 'GET'])
def table():
    if request.method == 'GET':
        cur.execute(f"SELECT * FROM tweets")
        rows = cur.fetchall()
    return render_template('table.html', items=rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)