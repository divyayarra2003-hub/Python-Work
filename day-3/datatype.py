count =7
count
7
type(count)
<class 'int'>
flt = 6.77
flt
6.77
type(flt)
<class 'float'>
cmplx = 7+9j
cmplx
(7+9j)
type(cmplx)
<class 'complex'>
str = 'heloooo'
str2 = "string type"
str
'heloooo'
str2
'string type'
type(str)
<class 'str'>
type(str2)
<class 'str'>
l = []
l2 = list()
l
[]
l2
[]
l=[3,5,7,9.678,"list string",["list of lists",7,5495]]
l
[3, 5, 7, 9.678, 'list string', ['list of lists', 7, 5495]]
type(l)
<class 'list'>
>>> t = (6,7,8,965,"tuple",True)
>>> t
(6, 7, 8, 965, 'tuple', True)
>>> type(t)
<class 'tuple'>
>>> s = {6,6,7,7,"set",False}
>>> s
{False, 7, 'set', 6}
>>> type(s)
<class 'set'>
>>> dict = {"Name":"codegnan","batch":5,"course":"PFS"}
>>> dict
{'Name': 'codegnan', 'batch': 5, 'course': 'PFS'}
>>> type(dict)
<class 'dict'>
>>> bool = True
>>> bool1 =False
>>> bool
True
>>> bool2
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    bool2
NameError: name 'bool2' is not defined. Did you mean: 'bool'?
>>> bool1
False
>>> type(bool)
<class 'bool'>
>>> some = None
>>> type(some)
<class 'NoneType'>
>>> some
>>> s1 = frozenset()
>>> s1(4,5,65,43,5)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s1(4,5,65,43,5)
TypeError: 'frozenset' object is not callable
>>> s1{6,4,5,90}
SyntaxError: invalid syntax
>>> s1 = frozenset({1,2,3,4})
>>> s1
frozenset({1, 2, 3, 4})
>>> type(s1)
<class 'frozenset'>