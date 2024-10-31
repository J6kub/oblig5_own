#Jakub B, no rights reserved
'''Examples on the bottom'''
import csv
import os
def is_floatable(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
assert is_floatable(10) == True
assert is_floatable(10.23) == True
assert is_floatable("10.34") == True
assert is_floatable("13") == True
assert is_floatable("pepe") == False
assert is_floatable(".") == False

class TableCsv:
    '''
    Bim bam
    '''
    def createRow(self, rawRow):
        '''Creates rows - Also used for inserting rows into Table'''
        '''ex row ["10,10,20,30,50,"rowrow"]'''
        '''Throws error if raw row is not length of header'''
        row = {}
        splitRowRaw = rawRow.split(self.splitterType)
        splitRow = []
        for elm in splitRowRaw:
            if is_floatable(elm):           #Floatifies every Cell if possible.
                splitRow.append(float(elm))
            else:
                splitRow.append(elm)
        for i in range(len(self.headish)):
            row[self.headish[i]] = splitRow[i]
        return row

    def __init__(self, csvFile, splitterType, progress=False, rowLimit=9999999999):
        '''Converting CSV file into a table'''
        self.path = csvFile
        if progress == True: print(f"Opening {csvFile}")
        file = open(csvFile,'r',encoding='utf-8')
        self.file = file.read()
        file.close()
        if progress == True: print("File opened!")
        self.rows = []
        self.splitterType = splitterType
        self.splitted = self.file.splitlines()
        if progress == True: print("File splitted into lines!")
        self.headish = self.splitted[0].split(self.splitterType)
        if progress == True: print("Header Loaded!")

        for x in range(1, len(self.splitted)):
            if x > rowLimit: break
            self.rows.append(self.createRow(self.splitted[x]))
            if progress == True: print(f"Row {x} loaded")
        self.splitted = None # Removes splitted for better Memory management

    def printItemTypes(self):
        '''Prints all headers'''
        for x in self.headish:
            print(x)
    def getItemTypes(self):
        '''Returns all headers in a list'''
        return self.headish
    def getRow(self,n):
        '''Returns Row N'''
        return self.rows[n]
    def getRowsByValue(self, htag, value):
        '''Returns Array of rows with the desired values'''
        rows = []
        for x in self.rows:
            if x[htag] == value:
                rows.append(x)
        return rows
    def getColumnList(self, column):
        '''Returns all values from a column'''
        res = []
        for row in self.rows:
            res.append(row[column])
        return res
    def printRows(self):
        '''Prints all rows'''
        for x in self.rows:
            print(x)
    def rowAppend(self,rr):
        '''Accepts Strings only!'''
        self.rows.append(self.createRow(rr))
    def rowDefenestrateByValue(self,htag,vall):
        '''Htag column name - Deletes items with the value'''
        self.rows = [x for x in self.rows if x[htag] != vall]
    def rowLeaveByValue(self,htag,vall):
        '''Htag column name - Deletes items with the value'''
        self.rows = [x for x in self.rows if x[htag] == vall]
    def rowDefenestrateN(self,index):
        '''Removes Row by index'''
        self.rows.pop(index)
    def saveTo(self,flname):
        '''Saves table to a specified CSV file.'''
        with open(flname, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headish, delimiter=';')
            writer.writeheader()
            writer.writerows(self.rows)
    def save(self):
        '''Saves table.'''
        with open(self.path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.headish, delimiter=';')
            writer.writeheader()
            writer.writerows(self.rows)
    def maxID(self):
        if len(self.rows) == 0: return 0
        sorte = sorted(self.rows, key=lambda x: x['id'], reverse=True)

        return int(sorte[0]['id'])

def CreateCsvTable(pth,hdrs, overwrite=None, progress=False):
    '''Input file name and path, and an array of headers'''
    if "." in pth:
        if pth.split(".")[len(pth.split("."))-1] != "csv":
            pth += ".csv"
    else:
        pth += ".csv"
    if os.path.exists(pth) and overwrite is None:
        raise ValueError("File already exists and might be overwritten! add overwrite=True as parameter")
    with open(pth, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=hdrs, delimiter=';')
        writer.writeheader()
    return TableCsv(pth, ";", progress=progress)


'''tbl = CreateCsvTable("csvTests",["id","c1","c2"], overwrite=True)         #- Creates a csv file and loads it into tbl variable
tbl.rowAppend("2,10,the one before was a float")     #- Adds a row
tbl.rowAppend("3,10,the one before was a float")
tbl.rowAppend("4,10,the one before was a float")
print(tbl.getRowsByValue("id",2))

tbl.save() '''                                               #- Saves the file
#tbl = TableCsv('DB_barn.csv',',')