#To Read Data
f = open("My Data","r")
print(f.readline())  #to print single line
print(f.read())

#To Write Data
f1 = open("abc","w")
f1.write("Laptop")

#To Append data
f1 = open("abc","a")
f1.write("Laptop")
f1.write("Mobile")

#To Copy Data from one file to Another
f = open("My Data","r")
f1 = open("abc","w")
for data in f:
    f1.write(data)