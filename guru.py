from kelas import kelas


class guru:

    def __init__(self, USER):
        self.USER = USER
        self.kelas = {}

    def getName(self):
        return self.USER.getName()

    def getUname(self):
        return self.USER.getUname()

    def getID(self):
        return self.USER.getID()

    def getMurid(self, KLS):
        return self.kelas[KLS]

    def getUserData(self):
        return self.USER.getUserData()

    """
    GURU memberi tugas ke suatu kelas
    semua murid dalam kelas itu mendapat 
    tugas yang sama
    """

    def giveTugas(self, namaKelas, namaTugas, desc='', dl=None):
        murids = self.kelas[namaKelas].getMember()
        self.kelas[namaKelas].addTugas(namaTugas, desc, dl)

        for murid in murids:
            murid.tugas[namaTugas] = 0

    def makeKelas(self):
        nama = input("Nama kelas: ")
        enrPresent = input("Menggunakan enrollment key? [y/n]: ")

        if enrPresent.lower() == 'y':
            enr = input("Enrollment key: ")
            self.kelas[nama] = kelas(nama, self, enr)

        else:
            if enrPresent.lower() != 'n':
                print("Error. Enrollment key dianggap tidak ada.")
            self.kelas[nama] = kelas(nama, self)

    def nilaiTugas(self):
        namaKelas = input("Nama kelas: ")
        if namaKelas not in self.kelas.keys():
            print("Nama kelas tidak ada.")
            return

        namaTugas = input("Nama tugas: ")
        if namaTugas not in self.kelas[namaKelas].tugass.keys():
            print("Nama tugas tidak ada.")
            return

        namaMurid = input("Nama murid: ")
        try:
            murid = self.kelas.members[namaMurid]
        except:
            print("Murid tidak terdaftar di kelas.")
        nilai = int(input("Nilai: "))
        self.kelas[namaKelas].tugass[namaTugas].setNilai(murid, nilai)