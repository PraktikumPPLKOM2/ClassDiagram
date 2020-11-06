import user.py

class ortu:

    def __init__(self,iD,uname,pw,name,noTelp,email,alamat):
        self.dataUser = user(uname,pw,name,noTelp,email,alamat)
        self.iD = iD
        self.anak = []

    def anak(self,ID):
        self.anak.append(ID)

    def getAnak(self):
        return self.anak

    def banyakAnak(self):
        return len(self.anak)

    def getUserData(self):
        return self.dataUser.getUserData

