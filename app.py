
from CSVtoTable import *

from flask import Flask, render_template, request
from init_db import *


app = Flask(__name__)


dicky = "dick"

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/potato')
def potato():
    return render_template('potato.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/oppgave')
def oppgave():
    return render_template('oppgave.html')
@app.route('/soknad')
def soknad():
    tbl.printRows()
    return render_template('soknad.html', data=tbl)
@app.route('/handlefood', methods=['POST'])
def handlefood():
    if request.method == 'POST':
        tbl.rowAppend(f"{request.form['food']},{request.form['number']}")
        tbl.save()
    return render_template('index.html')

@app.route('/commit')
def commit():
    return '<iframe width="560" height="315" src="https://www.youtube.com/embed/WbHGtGSwoGA?si=J5keRRIGpv74clcn&amp;controls=0&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
if __name__ == '__main__':
    app.run()
