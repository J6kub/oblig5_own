class soknad():
    def __init__(self, id):
        self.id = id

    def rawRow(self):
        return ""
class forelder():
    def __init__(id,navn,adresse,tlf,pnr):
        self.id = id
        self.navn = navn
        self.adresse = adresse
        self.tlf = tlf
        self.pnr = pnr
    def rawRow(self):
        return (",".join([str(self.id),self.navn,self.adresse,str(self.tlf),str(self.pnr)]))

class barn():
    def __init__(id,navn,pnr,fid):
        self.id = id
        self.navn = navn
        self.pnr = pnr
        self.foresatt_id = fid
    def rawRow(self):
        return ",".join([str(self.id),self.navn,str(self.pnr),str(self.foresatt_id)])