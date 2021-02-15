from flask import request, render_template
import requests
import urllib.request
import os
from flask import Flask

# initializations
app = Flask(__name__)
DAT = {'id': 1, "titulo": "garfield"}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_datos')
def get_datos():
    return DAT

@app.route('/sendDatos', methods=['POST'])
def sendDatos():
    if request.method == 'POST':
        id = request.form['id']
        titulo = request.form['titulo']
        dat = {'id': id, "titulo": titulo}
        print(id,titulo)
        DAT.update(dat)
        url = "http://localhost:8082"
        r = requests.get(url=url, params=dat)
        print(r)
        js = r.json()
        print(js)
        return render_template("index.html", datos=js)
    return render_template("error.html")

