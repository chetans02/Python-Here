'''
def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i,6):
            if nums [j]<nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [5,3,8,6,7,2]
sort(nums)
print(nums)'''
num = int(input("Enter a Number"))
temp = num
rev = 0
while num > 0 :
    dig = num %10
    rev = rev*10+dig
    num = num//10

if temp ==rev:
    print ("The number is Palindrome")
else:
    print ("Numebr is not a Palindrome")
