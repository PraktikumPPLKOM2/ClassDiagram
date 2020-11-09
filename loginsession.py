from user import user
from murid import murid
from ortu import ortu
from guru import guru

_usercollection = {}
userDatabase = {"Murid": [], "Guru": [], "Ortu": []}
_usercollection["doni"] = ["1","w@"]
_usercollection["salsa"] = ["2","2w"]
_usercollection["yohan"] = ["3","ew"]

class loginsession:

    def __init__(self):
        self._nama = ""
        self._uname = ""
        self._notelp = ""
        self._alamat = ""
        self._email = ""
        self._password = ""

    def register(self, azn):
        global _usercollection
        self._nama = input("Masukkan nama: ")
        self._uname = input("Masukkan Username: ")
        self._notelp = input("Masukkan nomor telepon (ex: 0812xxx): ")
        self._alamat = input("Masukkan alamat: ")
        while (True):
            self._email = input("Masukkan email: ")
            self._password = input("Masukkan password: ")
            repassword = input("Masukkan ulang password: ")
            # verification

            """
            ADD VERIFICATION IF EMAIL
            HAS BEEN USED OR NO
            """

            while (True):
                if self._email in list(_usercollection.keys()):
                    print("""
                    Maaf email sudah di pakai!
                    Mohon untuk login
                    Atau gunakan email lain!

                    1. Login
                    2. Ganti Email
                    """)
                    anss = int(input("Answer: "))
                    if anss == 1:
                        self.login()
                    elif anss == 2:
                        self._email = input("Masukkan ulang email: ")
                    else:
                        print("Input tidak diterima!")
                else:
                    break

            if ("@" in self._email and self._password == repassword):
                break
            elif (self._password != repassword):
                print("Password tidak sama!")
            else:
                print("Email tidak sesuai ketentuan!")

        _usercollection[self._uname] = [self._password, self._email]

        # SEND TO DATABSE FOR NEW USER
        xxx = user(self._uname, self._password, self._nama, self._notelp, self._email, self._alamat)

        if azn == 1:
            return murid(xxx)
        elif azn == 2:
            return guru(xxx)
        else:
            return ortu(xxx)

    def login(self, status):
        global _usercollection
        invalid = False
        while (True):
            username = input("Username: ")
            password = input("Password: ")
            index = 0
            # verification
            for i in range(len(userDatabase[status])):
                if (username == userDatabase[status][i].getUname()):
                    index = i
                    break
                else:
                    if (i == len(userDatabase) - 1):
                        invalid = True
                        break
            if (invalid == True):
                print("Username tidak ditemukan")
                continue

            if _usercollection[username][0] == password:
                # LOGIN SUCCESS
                print("Login Sukses")
                return index
                break
            else:
                # LOGIN FAILED
                print("password salah, silahkan coba lagi")
                # return False

    def forgotpassword(self):
        while (True):
            print("""
            Siapakah anda?
            1. Murid
            2. Guru
            3. Orang Tua
            """)
            status = int(input("Masukkan Pilihan anda: "))
            if (status > 3 or status < 1):
                continue
            else:
                str(status)
                if (status == "1"):
                    status = "Murid"
                elif (status == "2"):
                    status = "Guru"
                else:
                    status = "Ortu"
            theuser = input("Masukkan username: ")
            themail = input("Masukkan Email: ")
            if (themail == _usercollection[theuser][1]):
                print("Kami telah mengirim kode ke dalam email anda")
                print("(Untuk contoh, kode adalah: 1902)")
                code = "1902"
                thecode = input("Masukkan kode")
                if (code == thecode):
                    print("silahkan lakukan reset password")
                    # verification
                    while (True):
                        newpassword = input("Masukkan password baru: ")
                        renewpassword = input("Masukkan password baru sekali lagi: ")
                        if (newpassword == renewpassword):
                            _usercollection[theuser][0] = newpassword
                            for i in range(len(userDatabase[status])):
                                if (userDatabase[status][i].getUname() == theuser):
                                    userDatabase[status][i].pw = newpassword
                            print("Password telah berhasil diubah")
                            break
                        else:
                            print("password tidak cocok")
                    break
                else:
                    print("Kode salah")


            else:
                print("email yang dimasukkan tidak ditemukan")