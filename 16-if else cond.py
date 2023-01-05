
'''x = int(input("enter a no"))
r = x % 2

if r==0:
    print("Even")
else:
    print("Odd")
print("Bye")

x = int(input("enter a no"))
r = x % 2

if r==0:
    print("Even")
    if x>5:              # if inside if and else
        print('Greater')
    else:
        print('Lower')
else:
    print("Odd")
print("Bye")

#elif
x = int(input("Enter a No"))
if x==1:
    print("One")
elif x==2 :
    print("Two")
elif x == 3:
    print("Three")
elif x == 4:
    print("Four")
else:
    print("wrong input")

#Check no is Positive or Negative
x = int(input("Enter No"))
if x>=0:
    print("Positive No")
else:
    print("Negative No") '''




#Take three values from user & find the greatest no.from them
x = int(input("Enter No"))
y = int(input("Enter No"))
z = int(input("Enter No"))
if x>y:
    if x>z:
        print("X is Greater")


elif y>z:
    if y>x:
        print("Y is Greater")

elif z>x:
    if z>y:
        print("Z is Greater")


