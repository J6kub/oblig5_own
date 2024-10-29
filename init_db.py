# init database files
tbl_foresatt = None
tbl_barnehager = None
tbl_barn = None
tbl_soknad = None
tbl = None

from CSVtoTable import *
def init_db(print_progress=False):
    global tbl, tbl_foresatt, tbl_barnehager, tbl_barn, tbl_soknad
    try:
        tbl = CreateCsvTable("foodDB.csv", ["food","number"],progress=print_progress)
    except ValueError:
        tbl = TableCsv("foodDB.csv",",",progress=print_progress)
    #init foresatt DB
    try:
        tbl_foresatt = CreateCsvTable("DB_foresatt.csv", ["id", "navn", "adresse", "tlf", "pnr"],progress=print_progress)
    except ValueError:
        tbl_foresatt = TableCsv("DB_foresatt.csv",",",progress=print_progress)
    #init barnehage DB
    try:
        tbl_barnehager = CreateCsvTable("DB_barnehager.csv", ["id", "navn", "plasser", "barn"],progress=print_progress)
    except ValueError:
        tbl_barnehager = TableCsv("DB_barnehager.csv",",",progress=print_progress)
    #init barn DB
    try:
        tbl_barn = CreateCsvTable("DB_barn.csv", ["id", "navn", "pnr", "foresatt_id"],progress=print_progress)
    except ValueError:
        tbl_barn = TableCsv("DB_barn.csv",",",progress=print_progress)
    #init barn DB
    try:
        tbl_soknad = CreateCsvTable("DB_soknad.csv", ["id", "foresatt_id", "barn_id", "priority","priority_comment", "inntekt"],progress=print_progress)
    except ValueError:
        tbl_soknad = TableCsv("DB_soknad.csv",",",progress=print_progress)
init_db(True)
full_db = {
    "tbl_foresatt":tbl_foresatt,
    "tbl_barnehager":tbl_barnehager,
    "tbl_barn":tbl_barn,
    "tbl_soknad":tbl_soknad
}