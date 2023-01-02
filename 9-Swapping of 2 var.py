Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 6
>>> temp = a
>>> a= b
>>> b = temp
>>> print(a)
6
>>> print(b)
5
>>> 
>>> # by formula
>>> a = a+b
>>> b = a-b
>>> a = a-b
>>> print(a)
5
>>> print(b)
6
>>> 
>>> a = 5
>>> b = 6
>>> a = a+b
>>> b = a-b
>>> a = a-b
>>> print(a)
6
>>> print(b)
5
>>> 
>>> a = a+ba = a-b
SyntaxError: cannot assign to expression
>>> KeyboardInterrupt
>>> a = a^b
>>> b = a^b
>>> a = a^b
>>> print(a)
5
print(b)
6
up arrow
SyntaxError: incomplete input
up arrow
SyntaxError: incomplete input
a = 5
b = 4
a,b = b,a
print(a)
4
print(b)
5
