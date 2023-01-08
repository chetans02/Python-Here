
x=int(input("Enter number which will give you Factorical of Number:\n"))
def fact(n):
    a = 1
    for i in range(1,n+1):
        a = a*i
    return a
result = fact(x)
print(result)