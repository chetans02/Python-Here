#1
'''
class Computer:
    def __init__(self):
        self.name = ("Chetan")
        self.age = (22)
    def upate(self):
        self.age = 20

c1 = Computer()
c2 = Computer()
c1.name = "Krishna"
c1.age = 16
c2.upate() #It will Update the Value of C2
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age) '''


class Computer:
    def __init__(self):
        self.name = ("Chetan")
        self.age = (22)
    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False


c1 = Computer()
c1.age = 30
c2 = Computer()
if c1.compare(c2):
    print("They are Same")
else:
    print("They are Different")

print(c1.name)
print(c2.name)