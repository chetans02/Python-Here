
class Computer:

    def __init__(self,Cpu,Ram):
        self.Cpu = Cpu
        self.Ram = Ram

    def config(self):
        print("Config is ",self.Cpu, self.Ram)

com1 = Computer('i5',16)
com2 = Computer('Ryzen 3',8)


com1.config()
com2.config()