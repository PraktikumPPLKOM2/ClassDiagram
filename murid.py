class murid:
    
    def __init__(self,USER):
        self.USER = USER
        self.tugas={}
        self.kelas=None

    def getName(self):
        return self.USER.getName()

    def getID(self):
        return self.USER.getID()

    def getKelas(self):
        return self.kelas

    def getUserData(self):
        return self.USER.getUserData()

    def getTugas(self):
        return self.tugas.keys()

    def statusTugas(self,tugas):
        if tugas in self.tugas and self.tugas[tugas]==0:
            #BELUM DIKERJAKAN
            return False
        elif tugas in self.tugas and self.tugas[tugas]==1:
            #SUDAH DIKERJAKAN
            return True
        else:
            print("Tugas tidak ditemukan! Periksa ulang keyword")

    def kumpulTugas(self,tugas):
        if tugas in self.tugas and self.tugas[tugas]==0:
            self.tugas[tugas]=1
        elif tugas in self.tugas and self.tugas[tugas]==1:
            print ("Tugasnya sudah dikerjakan!")
        else:
            print ("Tugas tidak ditemukan! Periksa ulang keyword")

    def getAlert(self,alert):
        print (alert + "!!!")