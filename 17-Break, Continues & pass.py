
#Break
'''
av = 5
x = int(input("Enter no of Candy"))
i = 1
while i <=x:
    if i > av:
        print("Out of Stock")
        break
    print("Candy")
    i = i+1
print("Bye")

#Continue
for i in range(1,101):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)
print("Bye")'''

#Pass
for i in range(1,101):
    if (i%2!=0):
        pass
    else:
        print(i)
print("Bye")