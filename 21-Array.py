#1

from array import *
vals = array('i', [5,9,-8,4,2])
for i in range(len(vals)):
    print(vals[i])


#2 char
from array import *
vals = array('u', ['a','b','c','d'])
for i in range(len(vals)):
    print(vals[i])

#3 Old value of array into new array

from array import *
vals = array('i',[2,4,6,8,3])
newArr = array(vals.typecode,(a for a in vals))
for i in newArr:
    print(i)
#4 Old value of array squares into new array
from array import *
vals = array('i',[2,4,6,8,3])
newArr = array(vals.typecode,(a*a for a in vals))
for i in newArr:
    print(i)

#5 Using while loop
from array import *
vals = array('i',[2,4,6,8,3])
newArr = array(vals.typecode,(a*a for a in vals))
i = 0
while i < len(newArr):
    print(newArr[i])
    i = i+1

#6 Creating an Array and takiing Values from User

from array import *
arr = array('i',[])
n = int(input("Enter the Length of Array "))
for i in range(n):
    x = int(input("Enter the Next values"))
    arr.append(x)
print(arr)

#7 Creating an Array and takiing Values from User and Searching the Index no:

from array import *
arr = array('i',[])
n = int(input("Enter the length of Array"))
for i in range(n):
    x = int(input("Enter the Next values"))
    arr.append(x)
print(arr)

val = int(input("Enter the Search element"))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k = k+1

print(arr.index(val))   #Direct function to print index no


#Differnet ways to creating an Array
#i) Array
from numpy import *
arr = array([1,2,3 ,4])
print(arr.dtype)
print("Array",arr)

#ii)linspace
from numpy import *
arr = linspace(0,15,20)
print(arr.dtype)
print("linspace",arr)

#iii)arange
from numpy import *
arr = arange(1,15,2)
print(arr.dtype)
print("arange",arr)

#iv)logspace
from numpy import *
arr = logspace(1,40,5)
print(arr.dtype)
print("Logspace",arr)

#v)zeros
from numpy import *
arr = zeros(5,int)
print(arr.dtype)
print("zeros",arr)

#vi)ones
from numpy import *
arr = ones(5)
print(arr.dtype)
print("ones",arr)

#Adding 5 to a guven Array
from numpy import *
arr = array([1,2,3,4,5])
arr = arr+5
print(arr)

#Adding two arrays
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])
arr3 = arr1+arr2
print(arr3)

#Concatenate Two Array
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])
print(concatenate([arr1,arr2]))

#Copying an Array

#1)Simple
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))  #Same address for arr1 & arr2
print(id(arr2))



#2 Shallow Copy using view fn
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))  #Different address for arr1 & arr2 and  Same Output for arr1 & arr2
print(id(arr2))

#3 Deep Copy
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
arr1[1]=7

print(arr1)
print(arr2)
print(id(arr1))  #Different Output for arr1 & arr2
print(id(arr2))


#Question
#Adding Two Arrays using for loop
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = array([2,4,6,8,10,12,14])
for i in range(len(arr1)):
    sum = arr1[i]+ arr2[i]
    print(sum)

#2. find maximum value from array without using in-built function
from numpy import *
arr = array([1,8,3,4,5])
max = arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
        break
print(max)
