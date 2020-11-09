from user import user
from murid import murid
from ortu import ortu
from guru import guru

class loginsession():
    
    _usercollection={}
    
    def __init__(self):
        self._nama = ""
        self._uname = ""
        self._notelp = ""
        self._alamat = ""
        self._email = ""
        self._password = ""
    
    def register(self):
        self._nama = input("Masukkan nama: ")
        self._uname = input("Masukkan Username: ")
        self._notelp = input("Masukkan nomor telepon (ex: 0812xxx): ")
        self._alamat = input("Masukkan alamat: ")
        while(True):
            self._email = input("Masukkan email: ")
            self._password = input("Masukkan password: ")
            repassword = input("Masukkan ulang password: ")
            #verification
            if("@" in self._email and self._password == repassword):
                break
            elif(self._password != repassword):
                print("Password tidak sama!")
            else:
                print("Email tidak sesuai ketentuan!")
        
        _usercollection[self._uname]=[self._password,self._email]
        
       # xxx = user(self._uname,self._password,self._nama,self._notelp,self._email,self._alamat)
        
        print ("""
        Siapakah anda?
        1. Murid
        2. Guru
        3. Orang Tua
        """)
        while (True):
            ans = int(input("Answer: "))
            if ans < 4:
                if ans==1:
                    return _usercollection["Murid"].append(murid(user))
                elif ans==2:
                    return _usercollection["Guru"].append(guru(user))
                else:
                    return _usercollection["Ortu"].append(ortu(user))
            else:
                print ("Wrong input! Try again")
        
    def login(self):
        while(True):
            username = input("username: ")
            password = input("password: ")
            #verification
            if username in self._usercollection.keys():
                if self._usercollection[username] == password:
                    #LOGIN SUCCESS
                    print("Login Sukses")
                    #return True
                    break
                else:
                    #LOGIN FAILED
                    print("password salah, silahkan coba lagi")
                    #return False
                    
            else:
                print("username salah, silahkan coba lagi")
    
    #def forgotpassword(self):
    #    while(True):
    #        themail = input("Masukkan Email: ")
    #        if(themail in _usercollection.value())
            
            
        