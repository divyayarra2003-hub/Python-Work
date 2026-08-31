Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
dict = {"name":77}
int(dict)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    int(dict)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(dict)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    float(dict)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(dict)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    complex(dict)
TypeError: complex() first argument must be a string or a number, not 'dict'
str(dict)
"{'name': 77}"
list(dict)
['name']
tuple(dict)
('name',)
set(dict)
{'name'}
bool(dict)
True
n = 10
n
10
float(n)
10.0
complex(n)
(10+0j)
str(n)
'10'
list(n)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(n)
TypeError: 'int' object is not iterable
set(n)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set(n)
TypeError: 'int' object is not iterable
dict(n)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(n)
TypeError: 'dict' object is not callable
bool(dict)
True
flt = 10.7
flt
10.7
int(flt)
10
complex(flt)
(10.7+0j)
str(flt)
'10.7'
list(flt)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(flt)
TypeError: 'float' object is not iterable
tuple(flt)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(flt)
TypeError: 'float' object is not iterable
set(flt)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(flt)
TypeError: 'float' object is not iterable
dict(flt)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(flt)
TypeError: 'dict' object is not callable
bool(flt)
True
cmp = 10+7j
cmp
(10+7j)
int(cmp)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int(cmp)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(cmp)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    float(cmp)
TypeError: float() argument must be a string or a real number, not 'complex'
string(cmp)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    string(cmp)
NameError: name 'string' is not defined. Did you forget to import 'string'?
str(cmp)
'(10+7j)'
list(cmp)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list(cmp)
TypeError: 'complex' object is not iterable
tuple(cmp)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    tuple(cmp)
TypeError: 'complex' object is not iterable
set(cmp)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    set(cmp)
TypeError: 'complex' object is not iterable
dict(cmp)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict(cmp)
TypeError: 'dict' object is not callable
bool(cmp)
True
s = "12"
int(S)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    int(S)
NameError: name 'S' is not defined. Did you mean: 's'?
int(s)
12
float(s)
12.0
complex(s)
(12+0j)
list(s)
['1', '2']
tuple(s)
('1', '2')
set(s)
{'1', '2'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(s)
TypeError: 'dict' object is not callable
bool(s)
True
l =[1,"90"]
int(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
"[1, '90']"
set(l)
{1, '90'}
tuple(l)
(1, '90')
dict(l)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    dict(l)
TypeError: 'dict' object is not callable
bool(l)
True
tup = (3,"tuple")
int(tup)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(tup)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
>>> float(tup)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(tup)
TypeError: float() argument must be a string or a real number, not 'tuple'
>>> complex(tup)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    complex(tup)
TypeError: complex() first argument must be a string or a number, not 'tuple'
>>> str(tup)
"(3, 'tuple')"
>>> list(tup)
[3, 'tuple']
>>> set(tup)
{'tuple', 3}
>>> bool(tup)
True
>>> s3 = {4,"set",90}
>>> int(s3)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    int(s3)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
>>> float(s3)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    float(s3)
TypeError: float() argument must be a string or a real number, not 'set'
>>> complex(s3)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    complex(s3)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> str(s3)
"{90, 'set', 4}"
>>> list(s3)
[90, 'set', 4]
>>> tuple(s3)
(90, 'set', 4)
>>> bool(s3)
True
