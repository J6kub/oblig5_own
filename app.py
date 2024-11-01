
from CSVtoTable import *
from flask import Flask, render_template, request, redirect, url_for
from init_db import *

template_path = ""
app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template(f'{template_path}home.html')

@app.route('/potato')
def potato():
    print(str(",".join(['ass','10'])))
    return render_template('potato.html')
@app.route('/soknader')
def soknader():
    dataS = []
    for sook in tbl_soknad.rows:
        if is_floatable(sook['status']):
            sook_bhg = tbl_barnehager.getRowsByValue('id', int(sook['status']))[0]["navn"]
            sook_tbd = "Tilbud"
        else:
            sook_bhg = ""
            sook_tbd = "Avslag"
        if sook['fortrinnsrett'] == 'False': ftrS = 'Nei'
        else: ftrS = 'ja'
        sooki = {
            "id":int(sook['id']),
            "foresatt id":int(sook['foresatt_id']),
            "barn id":int(sook['barn_id']),
            "fortinnsrett":ftrS,
            "status":sook_tbd,
            "tilbud":sook_bhg,
            "fortrinnsrett Kommentar": sook['ftr_txt'],
        }
        dataS.append(sooki)

    return render_template(f'{template_path}soknader.html', data=dataS)

@app.route('/oppgave')
def oppgave():
    return render_template(f'{template_path}oppgave.html')

@app.route('/soknad')
def soknad():
    return render_template(f'{template_path}soknad.html', data=full_db)

@app.route('/handlefood', methods=['POST'])
def handlefood():
    if request.method == 'POST':
        #data = request.form --- refer POST data to a variable
        tbl.rowAppend(f"{request.form['food']},{request.form['number']}")
        tbl.save()
    return render_template(f'{template_path}index.html')

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

        ### handle empties
        try:
            ftr = pdata["ftr"]
        except:
            ftr = False
        try:
            ftr_txt = pdata["ftr_txt"]
        except:
            ftr_txt = "Ingen fortrinnsrett"
        try:
            sibs = pdata["kid_siblings"]
        except:
            sibs = False

        ###

        for i in pdata: print(i)
        ## Parent Creation / Handling
        parent = tbl_foresatt.getRowsByValue('pnr', int(pdata['pnr_f']))
        if len(parent) == 0:  # Tested % certified funkish :)
            parentObj = tbl_foresatt.createRow(f"{tbl_foresatt.maxID() + 1};{pdata['name_foresatt']};{pdata['adress']};{pdata['tlf']};{pdata['pnr_f']}")
            print(parentObj)
            tbl_foresatt.rows.append(parentObj)
        else: parentObj = parent[0]

        ## Kid Creation / Handling
        kid = tbl_barn.getRowsByValue('pnr', int(pdata['pnr_kid']))
        print(kid)
        if len(kid) == 0:
            print('addddddded chikld')
            kidObj = tbl_barn.createRow(f"{tbl_barn.maxID() + 1};{pdata['name_kid']};{pdata["pnr_kid"]};{parentObj['id']};0")
            tbl_barn.rows.append(kidObj)
        elif kid[0]['barnehage_id'] == 0 or len(kid) > 1:
            print('Noooot addddddded chikld')
            kidObj = kid[0]
        else:
            svar_string = "Barnet går allerede på barnehage!"
            return redirect(url_for('svar', data=svar_string))
        #print(kidObj)

        ## Soknad Creation / Handling
        pps = list(map(lambda x: f"prioritet{x}", list(range(1, 4))))
        bps = list(map(lambda x: tbl_barnehager.getRowsByValue('id', int(pdata[x]))[0], pps))
        #return bps
        #
        # Make a function that checks for siblings
        # Seach by foresatt_id in DB_barn, if name PNR is different,
        #
        sosken = tbl_barn.getRowsByValue('foresatt_id',int(kidObj["foresatt_id"])) # gets all children with same parent id
        sosken = list(filter(lambda obj: obj["pnr"] != int(kidObj["pnr"]), sosken))# fitlers out current child obj
        sosken_bhg = list( map(lambda x: x["barnehage_id"],sosken) )  # list of all sibiling barnehage_ids
        #return sosken_bhg
        skn_status = "avslag"
        #priority list iteration
        for bnh in bps:
            print(bnh)
            if bnh['plasser'] > bnh['barn'] or bnh["id"] in sosken_bhg or ftr:
                kidObj['barnehage_id'] = bnh['id']
                skn_status = bnh['id']
                bnh['barn'] += 1
                break
        if skn_status != "avslag":
            tildelt_barnehage = tbl_barnehager.getRowsByValue("id",kidObj['barnehage_id'])[0]['navn']

        #print(f'{tbl_soknad.maxID()+1},{parentObj["pnr"]},{kidObj["id"]},{ftr},{ftr_txt},{sibs},{pdata["inntekt"]},{pdata["prioritet1"]},{pdata["prioritet2"]},{pdata["prioritet3"]},{skn_status}')
        tbl_soknad.rowAppend(f'{tbl_soknad.maxID()+1};{parentObj["id"]};{kidObj["id"]};{ftr};{ftr_txt};{sibs};{pdata["inntekt"]};{pdata["prioritet1"]};{pdata["prioritet2"]};{pdata["prioritet3"]};{skn_status}')
        tbl_barn.save()
        tbl_barnehager.save()
        tbl_foresatt.save()
        tbl_soknad.save()

        # {kidObj.navn} har fått plass på
        if kidObj['barnehage_id'] == 0:
            svar_string = f"{kidObj['navn']} har ikke fått plass på noen av barnehagene"
        else:
            svar_string = f"{kidObj['navn']} har fått plass på {tildelt_barnehage}"
        return redirect(url_for('svar', data=svar_string))


@app.route('/svar')
def svar():
    data = request.args.get('data')
    return render_template(f'{template_path}svar.html', data=data)

@app.route('/adm_all_data')
def adm_all_data():
    return render_template(f'{template_path}adm_all_data.html',data=full_db)

@app.route('/commit')
def commit():
    return '<iframe width="560" height="315" src="https://www.youtube.com/embed/WbHGtGSwoGA?si=J5keRRIGpv74clcn&amp;controls=0&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
if __name__ == '__main__':
    app.run()
