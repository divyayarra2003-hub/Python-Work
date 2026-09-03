c='strings.py'
c
'strings.py'
c.startswith('str')
True
c.startswith('p')
False
c.endswith('python')
False
c.endswith('py')
True
c.islower()
True
c.isupper()
False
'IRIEI'.isupper()
True
c.isalpha()
False
'fhdkjfkj'.isalpha()
True
c.isalnum()
False
'the234fjd'.isalnum()
True
c.isspace()
False
'          '.isspace()
True
'h        '.isspace()
False
c.istitle()
False
'This Is Python'.istitle()
True
'THIS IS PYTHON'.istitle()
False
>>> c.isidentifier()
False
>>> 'my_var'isidentifier()
SyntaxError: invalid syntax
>>> 'my_var'.isidentifier()
True
>>> '_myvar'.isidentifier()
True
>>> 'my_var@'.isidentifier()
False
>>> 
>>> l=[]
>>> l=list()
>>> l=[4,79,"sri",{1,3,33333334},[345,{4,5,7}]]
>>> l
[4, 79, 'sri', {1, 3, 33333334}, [345, {4, 5, 7}]]
>>> type(l)
<class 'list'>
>>> l[1,3,5,7]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l[1,3,5,7]
TypeError: list indices must be integers or slices, not tuple
>>> l=[1,3,5,7]
>>> m=[2,4,6,8]
>>> l+m
[1, 3, 5, 7, 2, 4, 6, 8]
>>> l*3
[1, 3, 5, 7, 1, 3, 5, 7, 1, 3, 5, 7]
>>> l[3]
7
>>> l[-1]
7
>>> l[2:4]
[5, 7]
>>> l[::-1]
[7, 5, 3, 1]
>>> l[1:4:2]
[3, 7]