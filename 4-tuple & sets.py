Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = (21,36,14,25)
>>> tup
(21, 36, 14, 25)
>>> tup[1]
36
>>> tup[1] = 26
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1] = 26
TypeError: 'tuple' object does not support item assignment
>>> s = {121,98,77,54,34,98}
>>> s
{98, 34, 54, 121, 77}
>>> s{2}
SyntaxError: invalid syntax
>>>  s.pop(2)
...  
SyntaxError: unexpected indent
>>>  s.pop()
...  
SyntaxError: unexpected indent
>>> s.pop(2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s.pop(2)
TypeError: set.pop() takes no arguments (1 given)
