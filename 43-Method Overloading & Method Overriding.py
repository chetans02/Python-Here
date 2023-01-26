
#1Method Overloading:  Not use in Python
class Student:
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

s1 = Student()
print(s1.sum(5,9,6))
print(s1.sum(5,9))
print(s1.sum(5))


#2 Method Overriding:
class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show ")
a1 = B()
a1.show()