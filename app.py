
from CSVtoTable import *

from flask import Flask, render_template, request

# init database for food and number
try:
    tbl = CreateCsvTable("foodDB.csv", ["food","number"])
except ValueError:
    tbl = TableCsv("foodDB.csv",",")


app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/potato')
def potato():
    return render_template('potato.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/handlefood', methods=['POST'])
def handlefood():
    if request.method == 'POST':
        tbl.rowAppend(f"{request.form['food']},{request.form['number']}")
        tbl.save()
    return render_template('index.html')
if __name__ == '__main__':
    app.run()
