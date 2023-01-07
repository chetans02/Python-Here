
#1
a = 10
def something ():
    a = 15
    print("in fun",a)
something()
print("out side fun",a)
#Qutput: in fun = 10, outside fun= 15


#2 Using Keyword Global
a = 10
def something():
    global a
    a = 15
    print("in fun",a)
something()
print("outside fun",a)
#Qutput: in fun = 15, outside fun= 15


#3 Changing the values of Global Variable without changing the values of local var
a = 10
print(id(a))
def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print("in fun",a)
    globals()['a'] = 15
something()
print("outside fn",a)
 #Out put 2002935415312 , 2002935415312, in fun 9 ,outside fn 15
