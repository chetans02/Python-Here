#Filter

x = [2,3,4,5,6,7,8]
even = list(filter(lambda n : n%2==0,x)) #Creating direct fun
print("Filter",even)

#Map
nums = [1,2,3,4,5,6,7,8,9]
even = list(filter(lambda n:n%2 == 0,nums))
double = list(map(lambda n:n*2,even))
print("Map",double)

#Reduce
from functools import reduce
nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(lambda n:n%2==0,nums))
doubles = list(map(lambda n:n*2,evens))
sum = reduce(lambda a,b: a+b,doubles)
print("Reduce",sum)