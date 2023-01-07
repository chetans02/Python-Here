
n = int(input("Enter the Sequence No."))
def fib(n):
    a=0
    b=1
    c = a+b
    if n<0:
        print("Invalid No.")
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)

fib(n)
