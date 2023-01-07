#1
'''
def greet():
    print("Hello")
    print("Good Morning")
greet()

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d
result1,result2 = add_sub(5,4)
print(result1,result2)

#Functions Arguments:
def update(lst):
    print(id(lst))  #to check id

    lst[1]=20
    print(id(lst))  #to check id
    print("x",lst)
lst = [10,15,30]
print(id(lst))      #to check id
update(lst)
print("lst",lst)

#Keyword
def person(name,age):
    print(name)
    print(age-5)
person(age=28,name='Chetan') #using keyword age and name as sequance is not proper


def person(name,age=18):
    print(name)
    print(age)
person("chetan")
person("Chetan",28)

#Variable Length
def sum (a,*b):
    c = a
    for i in b:
        c = c+i
    print(c)
sum(5,6,34,78) '''

#Keyword variable length Argument
def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)
person("Chetan",age = 22, City = "Mumbai", mob = 957434337)