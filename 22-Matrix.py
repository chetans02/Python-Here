#Flattem
'''
from numpy import *
arr1 = array([
               [1,2,3],
               [4,5,6]
           ])
arr2 = arr1.flatten()
print(arr2)

#Reshape
from numpy import *
arr1 = array([
          [1,2,3,4,5,6],
          [7,8,9,10,11,12]

])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,3)
print(arr3) '''

#diagonal
from numpy import *
m = matrix('1 2 3 ; 4 5 6 ; 7 8 9 ')
print(m.diagonal())
print(m.min())