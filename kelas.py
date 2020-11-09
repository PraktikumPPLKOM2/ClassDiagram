from tugas import tugas

totalKelas = 0

class kelas:
    """CLASS KELAS"""
    #normally kelas kan ada orang yg megang min 1.
    #jadi default guru yg ngisi itu adalah pemilik/teacher.
    def __init__(self, nama, guru, enr=None):
        global totalKelas
        totalKelas += 1
        self.id = totalKelas
        self.nama = nama
        self.teachers = [guru]
        self.members = []
        self.tugass = []
        self.enrollment = enr

    def getNama(self):
        return self.nama

    def addMember(self, murid, enr):
        if self.enrollment == None or enr == self.enrollment:
            self.members.append(murid)
            murid.kelas = self.nama
        else:
            print('Enrollment salah.')

    def getMembers(self):
        return self.members

    def addTeacher(self, guru):
        self.teachers.append(guru)

    def getTeachers(self):
        return self.teachers

    def addTugas(self, nama, desc='', dl=None):
        t = tugas(nama, desc, dl)
        self.tugass.append(t)

    def getTugas(self):
        return self.tugass