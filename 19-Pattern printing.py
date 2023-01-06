
#1
'''
for i in range(4):
    for j in range(4):
        print("#",end="")
    print()

#2
for i in range(4):
    for j in range(i+1):
        print("#",end="")
    print()

#3
for i in range(4):
    for j in range(4):
        if j >= i:
            print("#", end="")

    print()

#4
x = int(input("enter no or rows"))
for i in range(x):
    for j in range(x-i):
        print(j+i+1, end=" ")
    print()'''

#5
j1='ABCD'
j2='PQR'
for i in range(4):
    print(j1[:i+1]+j2[i:])
