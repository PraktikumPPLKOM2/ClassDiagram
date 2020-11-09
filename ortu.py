from murid import murid

class ortu:

    def __init__(self, USER):
        self.USER = USER
        self.anak = {}

    def getName(self):
        return self.USER.getName()

    def setAnak(self, murid):

        if murid.getName() in self.anak:
            print("Nama anak sudah ada!")
        else:
            self.anak[murid.getName()] = murid.getID()

    def getAnak(self):
        return self.anak.keys()

    def banyakAnak(self):
        return len(self.anak.keys())

    def getUserData(self):
        return self.USER.getUserData()

    def giveAlert(self, text, murid):
        print("Alert Set!")
        murid.getAlert(text)

    def tugasAnak(self, murid):
        return murid.tugas.keys()

    def getUname(self):
        return self.USER.getUname()

    def statusTugasAnak(self, murid):
        for key in murid.tugas:
            if murid.tugas[key] == 0:
                temp = "Belum dikerjakan"
            else:
                temp = "Sudah dikerjakan"
            print("""
            Nama      : %s
            Kelas     : %s
            Tugas     : %s
            Status    : %s
            """ % (murid.getName, murid.getKelas, key, temp))

    def nilai(self, tugas):
        return tugas.getNilai()