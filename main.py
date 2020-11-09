from sys import exit
from loginsession import loginsession, userDatabase
from user import user
from murid import murid
from guru import guru
from ortu import ortu

"""LOGIN SESSION"""
newuser = loginsession()

Doni = user("doni","1","doni","1","w@","ww")
Salsa = user("salsa","2","salsa","2","e@","2w")
Yohan = user("yohan","3","yohan","3","r@","ew")

userDatabase["Guru"].append(guru(Doni))
userDatabase["Murid"].append(murid(Salsa))
userDatabase["Ortu"].append(ortu(Yohan))

print("SELAMAT DATANG ")
while True:  # stop looping only when successfully login
    print('''
    1. Login
    2. Register
    3. Forgot Password
    4. Keluar
    ''')

    a = input("masukkan pilihan anda: ")

    if a == "1":
        print("""
        Siapakah anda?
        1. Murid
        2. Guru
        3. Orang Tua
        """)
        ans = int(input("Answer: "))
        x = 0
        if ans < 4:
            if ans == 1:
                x = ans
                ans = "Murid"
                i = newuser.login(ans)
            elif ans == 2:
                x = ans
                ans = "Guru"
                i = newuser.login(ans)
            else:
                x = ans
                ans = "Ortu"
                i = newuser.login(ans)
            # ini adalah user

            therealuser = userDatabase[ans][i]
            print(therealuser.getName())

            while (True):
                # Murid
                if x == 1:
                    a = input("kelas,tugas,status,kumpul,alert")
                    if a == "kelas":
                        therealuser.getKelas()
                    elif a == "tugas":
                        therealuser.getTugas()
                    elif a == "status":
                        b = input(therealuser.getTugas())
                        therealuser.statusTugas(b)
                    elif a == "kumpul":
                        c = input(therealuser.getTugas())
                        therealuser.kumpulTugas(c)
                    elif a == "alert":
                        therealuser.getAlert()
                    else:
                        print("Wrong input! Try again")


                #Guru
                if x == 2:
                    a = input("tugas,kelas,nilai")
                    if a == "tugas":
                        b = input("Nama kelas")
                        c = input("Nama tugas")
                        therealuser.giveTugas(b,c)
                    elif a == "kelas":
                        therealuser.makeKelas()
                    elif a == "nilai":
                        therealuser.nilaiTugas()
                    else:
                        print("Wrong input! Try again")

                #Ortu

                if x == 3:
                    a = input("set,list,banyak,data,alert,tugas,uname,status,nilai")
                    if a == "set":
                        murid = input('nama anak: ')
                        for i, obj in enumerate(userDatabase['Murid']):
                            if obj.getName() == murid:
                                exec('therealuser.setAnak(userDatabase["Murid"][' + str(i) + '])')
                    elif a == "list":
                        print(therealuser.getAnak())
                    elif a == "banyak":
                        print(therealuser.banyakAnak())
                    elif a == "data":
                        therealuser.getUserData()
                    elif a == "alert":
                        therealuser.giveAlert()
                    elif a == "tugas":
                        therealuser.tugasAnak()
                    elif a == "uname":
                        therealuser.getuname()
                    elif a == "status":
                        therealuser.statusTugasAnak()
                    elif a == "nilai":
                        therealuser.nilai()
                    else:
                        print("Wrong input! Try again")

    elif a == "2":
        print("""
        Siapakah anda? 
        1. Murid
        2. Guru
        3. Orang Tua
        """)
        ans = int(input("Answer: "))
        if ans < 4:
            i = newuser.register(ans)
            if ans == 1:
                userDatabase["Murid"].append(i)
            elif ans == 2:
                userDatabase["Guru"].append(i)
            elif ans == 3:
                userDatabase["Ortu"].append(i)
        else:
            print("Wrong input! Try again")

    elif a == "3":
        newuser.forgotpassword()

    elif a == "4":
        print("Sampai jumpa lagi")
        exit()

    else:
        print("salah memasukkan pilihan")

"""MAIN PROGRAM"""
print('main program')