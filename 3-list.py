Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
nums = [25,30,26,18,3,6]
nums
[25, 30, 26, 18, 3, 6]
nums[0]
25
nums[6]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    nums[6]
IndexError: list index out of range
nums[5]
6
nums[:6]
[25, 30, 26, 18, 3, 6]
nums[5:]
[6]
KeyboardInterrupt
nums[:5]
[25, 30, 26, 18, 3]
>>> nums[-1]
6
>>> nums[-6]
25
>>> names = ['Chetan','Vaishnavi','Kartik']
>>> names
['Chetan', 'Vaishnavi', 'Kartik']
>>> values = ['9.5', 'Chetan', '26']
>>> values
['9.5', 'Chetan', '26']
>>> mil = [nums, names]
>>> mil
[[25, 30, 26, 18, 3, 6], ['Chetan', 'Vaishnavi', 'Kartik']]
>>> mil = [nums, names, values]
>>> mil
[[25, 30, 26, 18, 3, 6], ['Chetan', 'Vaishnavi', 'Kartik'], ['9.5', 'Chetan', '26']]
>>> nums.append(45)
>>> nums
[25, 30, 26, 18, 3, 6, 45]
>>> nums.insert(2,77)
>>> nums
[25, 30, 77, 26, 18, 3, 6, 45]
>>> nums.pop(1)
30
>>> nums.pop()
45
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29,12,14,36])
>>> nums
[25, 77, 29, 12, 14, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
