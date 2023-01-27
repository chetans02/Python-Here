
#while loop
pos = -1
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()["pos"] = i
            return True
        i = i+1
    return False


list  = [2,5,8,9,4]
n = int(input("Enter a No"))
if search(list,n):
    print("While Loop  Found at",pos+1)
else:
    print("Not found")


#For loop
pos = -1
def search(list,n):
    i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals()["pos"] = i
            return True
    return False


list  = [2,5,8,9,4]
n = int(input("Enter a No"))
if search(list,n):
    print("For Loop  Found at",pos+1)
else:
    print("Not found")



