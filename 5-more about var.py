Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 5
>>> id(num)
1961164079472
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
1961164079632
>>> id(b)
1961164079632
>>> id(10)
1961164079632
>>> k = 10
>>> id(k)
1961164079632
>>>  a= 9
...  
SyntaxError: unexpected indent
>>> a = 9
>>> id(a)
1961164079600
>>> id(b)
1961164079632
>>>  k = a
...  
SyntaxError: unexpected indent
>>> k = a
>>> id(a)
1961164079600
>>> b = 8
>>> id(b)
1961164079568
