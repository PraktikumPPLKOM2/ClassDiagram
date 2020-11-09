totalKelas = 0
from tugas import tugas

class kelas:
    """CLASS KELAS"""
    def __init__(self, nama, guru, enr=None):
        global totalKelas
        totalKelas += 1
        self.id = totalKelas
        self.nama = nama
        self.teachers = {}
        self.teachers[guru.getName()] = guru
        self.members = {}
        self.tugass = {}
        self.enrollment = enr

    def getNama(self):
        return self.nama

    def addMember(self, murid, enr):
        if self.enrollment == None or enr == self.enrollment:
            self.members[murid.getName()] = murid
            murid.kelas = self
        else:
            print('Enrollment salah.')

    def getMembers(self):
        return self.members

    def addTeacher(self, guru):
        self.teachers[guru.getName()] = guru

    def getTeachers(self):
        return self.teachers

    def addTugas(self, nama, desc, dl):
        self.tugass[nama] = tugas(nama, desc, dl)
        for member in self.members:
            member.getAlert(
                'Tugas - '
                + nama
                + ':'
                + self.nama
                + 'ditambahkan'
                )

    def getTugas(self):
        return self.tugass