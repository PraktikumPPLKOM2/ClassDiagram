from kelas import kelas

class guru:
    
    def __init__(self,USER):
        self.USER=USER
        
    def getName(self):
        return self.USER.getName()

    def getID(self):
        return self.USER.getID()

    def getMurid(self,KLS):
        return self.kelas[KLS]

    def getUserData(self):
        return self.USER.getUserData()
        
    """
    GURU memberi tugas ke suatu kelas
    semua murid dalam kelas itu mendapat 
    tugas yang sama
    """
    def giveTugas(self,kelas,tugas):
        murids = kelas.getMember()
        kelas.tugass.append(tugas)
        for i in range (len(murids)):
            #ASSIGN ASSESSMENT
            murid.tugas[tugas] = 0
            #0 UNTUK BELUM DIKERJAKAN
    
    