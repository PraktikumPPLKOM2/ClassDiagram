from loginsession import loginsession
import kelas

# MAIN

usercollection = {}

# REGISTRASI 
newuser = loginsession()
newuser.registrasi()

usercollection["Guru"] = newuser
# Guru memberi tugas

