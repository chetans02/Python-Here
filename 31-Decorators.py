#without Decorators
'''def div(a,b):
    if a<b:
        a,b=b,a
    print(a/b)
div(2,4)'''

#Using Decorators
a = int(input("Enter a No 1"))
b = int(input("Enter a No 2"))

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(a,b)