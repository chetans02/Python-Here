
#1 Instance Method

class Student:
    student = "RWTH"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):    #Instance Method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self):
        return self.m1

s1 = Student(34,47,32)
s2 = Student(25,13,70)

print(s1.avg())
print(s1.set_m1())

#2 Class Method
class Student:
    school = "RWTH"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):    #Instance Method
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

s1 = Student(34,47,32)
s2 = Student(25,13,70)

print(s1.avg())
print(Student.info())

#Static Method
class Student:
    school = "RWTH"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):    #Instance Method
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def get_School(cls):
        return cls.school

    @staticmethod
    def info():
        print("This student class...in abc Module")

s1 = Student(34,47,32)
s2 = Student(25,13,70)

print(s1.avg())
print(Student.get_School())
Student.info()