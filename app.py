
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
        #data = request.form --- refer POST data to a variable
        tbl.rowAppend(f"{request.form['food']},{request.form['number']}")
        tbl.save()
    return render_template('index.html')

@app.route('/handlesoknad', methods=['POST'])
def handlesoknad():
    '''
    Use tbl.createRow to create Object of given type barn,soknad,foresatt
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
        pdata = request.form
        for i in pdata: print(i)
        ## Parent Creation / Handling
        parent = tbl_foresatt.getRowsByValue('pnr', pdata['pnr_f'])
        if len(parent) == 0:
            parentObj = tbl_foresatt.createRow(f"{tbl_foresatt.maxID() + 1},{pdata['name_foresatt']},{pdata['adress']},{pdata['tlf']},{pdata['pnr_f']}")
            print(parentObj)
        else: parentObj = parent[0]

        ## Kid Creation / Handling
        kid = tbl_barn.getRowsByValue('pnr', pdata['pnr_kid'])
        if len(kid) == 0:
            kidObj = tbl_barn.createRow(f"{tbl_barn.maxID() + 1},{pdata['name_kid']},{pdata["pnr_kid"]},{parentObj['id']},0")
        elif kid[0].barnehage_id == 0:
            kidObj = kid[0]
        else:
            return "Barnet går allerede på barnehage"
        print(kidObj)

        ## Soknad Creation / Handling
        pps = list(map(lambda x: f"prioritet{x}", list(range(1, 4))))
        bps = list(map(lambda x: tbl_barnehager.getRowsByValue('id', int(pdata[x]))[0], pps))
        return bps
        #
        # Make a function that checks for siblings
        # Seach by foresatt_id in DB_barn, if name PNR is different,
        #


        """for bnh in bps:
            if bnh.plasser > bnh.barn:
                kid has a place!"""


            ## approve child


@app.route('/commit')
def commit():
    return '<iframe width="560" height="315" src="https://www.youtube.com/embed/WbHGtGSwoGA?si=J5keRRIGpv74clcn&amp;controls=0&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
if __name__ == '__main__':
    app.run()
