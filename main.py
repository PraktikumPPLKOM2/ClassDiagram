from loginsession import loginsession
import kelas

# MAIN

user = {}

newuser = loginsession()

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

