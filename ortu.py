from user import user

class ortu:

    def __init__(self,iD,uname,pw,name,noTelp,email,alamat):
        self.dataUser = user(uname,pw,name,noTelp,email,alamat)
        self.iD = iD
        self.__anak = []

    def anak(self,ID):
        self.__anak.append(ID)

    def getAnak(self):
        return self.__anak

    def banyakAnak(self):
        return len(self.__anak)

    def getUserData(self):
        return self.dataUser.getUserData

