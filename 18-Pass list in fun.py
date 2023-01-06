#1
'''
from array import *
arr = array('i',[])
n = int(input("Enter the length of the array: "))
for i in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)
print(arr)
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if 1%2 == 0:
            even = even+1
        else:
            odd = odd+1
    return even,odd
even,odd = count(lst)
print("Even:{} and Odd:{}".format(even,odd)) '''

#2
lst = list()
n = int(input('enter the no. of names:'))
for i in range(n):
    val = input('enter the list of names:')
    lst.append(val)
print(lst)
def names(lst):
    for i in lst:
        if(len(i)>=5):
            print(i,':greater than 5 letters')
        else:
            print(i,':less than 5 letters ')
names(lst)
