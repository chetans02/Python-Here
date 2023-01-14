
#Single Inheritance:

class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 workng")
    def feature2(self):
        print("Fetature 2 working")
class B(A):

    def __init__(self):
        super(). __init__()
        print("in B init")
    def feature3(self):
        print("Feature 3 working ")
    def feature4(self):
        print("Feature 4 working")
a1 = B()


#Multilevel Inheritance:
class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 workng")
    def feature2(self):
        print("Fetature 2 working")
class B:
    def __init__(self):
        print("in B init")
    def feature3(self):
        print("Feature 3 working ")
    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")
    def feature5(self):
        print("Feature 5 working")

    def feat(self):   #Super method to call different feature
        super().feature2()
a1 = C()     #It will print Class A init & Class C, i.e from left to right
a1.feat()