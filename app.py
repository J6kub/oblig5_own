
from CSVtoTable import *
from classes import *
from flask import Flask, render_template, request
from init_db import *


app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/potato')
def potato():
    print(str(",".join(['ass','10'])))
    return render_template('potato.html')
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/oppgave')
def oppgave():
    return render_template('oppgave.html')

@app.route('/soknad')
def soknad():
    return render_template('soknad.html', data=full_db)

@app.route('/handlefood', methods=['POST'])
def handlefood():
    if request.method == 'POST':
        tbl.rowAppend(f"{request.form['food']},{request.form['number']}")
        tbl.save()
    return render_template('index.html')

@app.route('/handlesoknad', methods=['POST'])
def handlesoknad():
    '''
    Tactical Script!
    Gather data from form
    Check for duplicates pnr_f in DB_foresatt["pnr"]
    Check for duplicates name_kid in DB_barn["navn"]

    Append if not duplicates***

    soknad(
    id <- try: max(tbl_soknad.getColumnList("id") error: 0
    foresatt_
    )

    '''

    if request.method == 'POST':
        print('Shit')
@app.route('/commit')
def commit():
    return '<iframe width="560" height="315" src="https://www.youtube.com/embed/WbHGtGSwoGA?si=J5keRRIGpv74clcn&amp;controls=0&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
if __name__ == '__main__':
    app.run()
