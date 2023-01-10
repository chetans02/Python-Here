
class Car:
    wheels = 4  # Class Variable
    def __init__(self):
        self.mil = 10 #Instance Variable
        self.comp = "BMW" #Instance Variable
c1 = Car()
c2 = Car()
Car.wheels = 5 #To change Calss Variable
c1.mil = 8
print(c1.mil, c1.comp, c1.wheels)
print(c2.mil, c2.comp, c2.wheels)