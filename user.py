class user:

    def __init__(self,uname,pw,name,noTelp,email,alamat):
        self.uname = uname
        self.pw = pw
        self.name = name
        self.noTelp = noTelp
        self.email = email
        self.alamat = alamat

    def getUserData(self):
        print("""
        Username = %s
        Name     = %s
        No Telp  = %s
        Email    = %s
        Alamat   = %s
        """)

    def getUname(self):
        return self.uname

    def getPw(self):
        return self.pw

    def getName(self):
        return self.name

    def getNoTelp(self):
        return self.noTelp

    def getEmail(self):
        return self.email

    def getAddress(self):
        return self.alamat
