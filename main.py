from loginsession import loginsession
import kelas

# MAIN

# Login Session
newuser = loginsession()
while(True):
    print("SELAMAT DATANG ")
    print('''
    1. Login
    2. Register
    3. Forgot Password
    4. keluar
    ''')
    a = input("masukkan pilihan anda: ")
    if (a == "1"):
        newuser.login()
    elif (a == "2"):
        newuser.register()
    elif (a == "3"):
        newpass = newuser.forgotpassword()

    elif(a==4):
        print("Sampai jumpa lagi")
        break
    else:
        print("salah memasukkan pilihan")


'''
# GURU
newuser.register()
user["Guru"] = newuser
newuser.login()

# MURID
newuser.register()
user["Murid"] = newuser
newuser.login()

# ORTU
newuser.register()
user["Ortu"] = newuser
newuser.login()
'''