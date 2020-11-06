import user.py

class murid:

    def __init__(self,iD,kelas,tugas,uname,pw,name,noTelp,email,alamat):
        self.dataUser = user(uname,pw,name,noTelp,email,alamat)
        self.iD = iD
        self.kelas = kelas
        self.tugas = tugas

    def getID(self):
        return self.iD

    def getKelas(self):
        return self.kelas

    def getTugas(self):
        return self.tugas

    def addTugas(self,newTugas):
        self.tugas.append(newTugas)

    #def statusTugas(self,status):
    #    if status == 0:

