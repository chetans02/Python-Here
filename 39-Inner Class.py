
class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.Lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.Lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 6
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student("Krishna",1)
s2 = Student("Chetan",2)
s1.show()