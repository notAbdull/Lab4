# ----- Ibrahim BinZaid 442105987-----#
#P1
class Course:

    def __init__(self, cd, ca, co, sn):
        self.Code = cd
        self.Capacity = ca
        self.Core = co
        self.StudentsNo = sn

    def __str__(self):
        return '(Code = ' + self.Code + ', Capacity = ' + str(self.Capacity) + \
        ', Core = ' + str(self.Core) + ', StudentsNo = ' + str(self.StudentsNo) + ')'

