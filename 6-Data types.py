Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num = 5
typ(num)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    typ(num)
NameError: name 'typ' is not defined. Did you mean: 'type'?
type(num)
<class 'int'>
num = 2.5
type(num)
<class 'float'>
a =5
a =5
a  = 5.6
b = float(a)
b
5.6
b = int(a)
b
5
k = float(b)
k
5.0

k = 6
c = complex(b,k)
c
(5+6j)
type(c)
<class 'complex'>
b<k
True
b>k
False
int(true)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
int(True)
1
int(False)
0

lst = [23,45,67,26,18]
type(lsy)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    type(lsy)
NameError: name 'lsy' is not defined. Did you mean: 'lst'?
type(lst)
<class 'list'>

>>> s = {23,87,90,45}
>>> type(s)
<class 'set'>
>>> 
>>> t = (23,56,40,56)
>>> type(t)
<class 'tuple'>
>>> 
>>> str = "Chetan"
>>> type(str)
<class 'str'>
>>> 
>>> 
>>> 

>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> 
>>> d = {'Chetan': 'Samsung', 'Krishna': 'IPhone', 'Balram': 'Oneplus'}
>>> d
{'Chetan': 'Samsung', 'Krishna': 'IPhone', 'Balram': 'Oneplus'}
>>> d.keys
<built-in method keys of dict object at 0x0000013F58B08C00>
>>> d.keys()
dict_keys(['Chetan', 'Krishna', 'Balram'])
>>> d.values()
dict_values(['Samsung', 'IPhone', 'Oneplus'])
>>> d.get('Krishna')
'IPhone'
>>> d['Balram']
'Oneplus'
