#Factirial using Recursion
x = int(input("Enter a number to find Factorial:\n"))
def fact(n):
    if(n==0):
        return 1
    return n * fact(n-1)
result = fact(x)
print(result)