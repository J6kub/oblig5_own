'''Koden bruker min CSVtoTable modul for å lage og loade inn database system som er satt opp av flere csv filer som
tilsvarer excel sheets'''

splitter = ';'
db_path = 'db/'
# init database files
tbl_foresatt = None
tbl_barnehager = None
tbl_barn = None
tbl_soknad = None

from CSVtoTable import *
def init_db(print_progress=False):
    global tbl_foresatt, tbl_barnehager, tbl_barn, tbl_soknad
    #init foresatt DB
    try:
        tbl_foresatt = CreateCsvTable(db_path + "DB_foresatt.csv", ["id", "navn", "adresse", "tlf", "pnr"],progress=print_progress)
    except ValueError:
        tbl_foresatt = TableCsv(db_path + "DB_foresatt.csv",splitter,progress=print_progress)
    #init barnehage DB
    try:
        tbl_barnehager = CreateCsvTable(db_path + "DB_barnehager.csv", ["id", "navn", "plasser", "barn"],progress=print_progress)
        tbl_barnehager.rowAppend("1;Boblestien Barnehage;150;70")
        tbl_barnehager.rowAppend("2;Fangsheng Barnehage;23;22")
        tbl_barnehager.rowAppend("3;Kakerlakker Hage;250;120")
        tbl_barnehager.rowAppend("4;Barnepoliti skolen;100;100")
        tbl_barnehager.rowAppend("5;Abc 123 hagebarn;101;102")
        tbl_barnehager.save()
    except ValueError:
        tbl_barnehager = TableCsv(db_path + "DB_barnehager.csv",splitter,progress=print_progress)
    #init barn DB
    try:
        tbl_barn = CreateCsvTable(db_path + "DB_barn.csv", ["id", "navn", "pnr", "foresatt_id","barnehage_id"],progress=print_progress)
    except ValueError:
        tbl_barn = TableCsv(db_path + "DB_barn.csv",splitter,progress=print_progress)
    #init barn DB
    try:
        tbl_soknad = CreateCsvTable(db_path + "DB_soknad.csv", ["id", "foresatt_id", "barn_id", "fortrinnsrett","ftr_txt","sosken","inntekt","p1","p2","p3","status"],progress=print_progress)
    except ValueError:
        tbl_soknad = TableCsv(db_path + "DB_soknad.csv",splitter,progress=print_progress)
init_db(True)


full_db = {
    "tbl_foresatt":tbl_foresatt,
    "tbl_barnehager":tbl_barnehager,
    "tbl_barn":tbl_barn,
    "tbl_soknad":tbl_soknad
}