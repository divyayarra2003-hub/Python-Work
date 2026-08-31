Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[10,9,6,1,2,3,4]
l
[10, 9, 6, 1, 2, 3, 4]
id(l)
3145688184576
l.append(12)
l
[10, 9, 6, 1, 2, 3, 4, 12]
l.append(14)
l
[10, 9, 6, 1, 2, 3, 4, 12, 14]
id(l)
3145688184576
l.insert(1,7)
l
[10, 7, 9, 6, 1, 2, 3, 4, 12, 14]
l.extend([70,90,44])
l
[10, 7, 9, 6, 1, 2, 3, 4, 12, 14, 70, 90, 44]
l[3] = 70
l
[10, 7, 9, 70, 1, 2, 3, 4, 12, 14, 70, 90, 44]
l.pop()
44
l
[10, 7, 9, 70, 1, 2, 3, 4, 12, 14, 70, 90]
l.remove(2)
l
[10, 7, 9, 70, 1, 3, 4, 12, 14, 70, 90]
l.remove(70)
l
[10, 7, 9, 1, 3, 4, 12, 14, 70, 90]
l.pop(1)
7
del l[-1]
l
[10, 9, 1, 3, 4, 12, 14, 70]
l.clear()
l
[]
id(l)
3145688184576
max(l)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    max(l)
ValueError: max() iterable argument is empty
l=[7,90,70,50,232,789]
l
[7, 90, 70, 50, 232, 789]
max(l)
789
min(l)
7
sorted(l)
[7, 50, 70, 90, 232, 789]
l.reverese()
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    l.reverese()
AttributeError: 'list' object has no attribute 'reverese'. Did you mean: 'reverse'?
l.reverse()
l
[789, 232, 50, 70, 90, 7]
l.sort()
l
[7, 50, 70, 90, 232, 789]
l.sort(reverse=True)
l
[789, 232, 90, 70, 50, 7]
sum(l)
1238
l=[7,45,4]
m=[7,45,4]
l
[7, 45, 4]
n=l
n.append(7)
n
[7, 45, 4, 7]
l
[7, 45, 4, 7]
n=l.copy()
n.append(77)
n
[7, 45, 4, 7, 77]
l
[7, 45, 4, 7]
all([0,'',[],{},(),set(),False])
False
>>> all([1,'',[],{},(),set(),False])
False
>>> any([1,'',[],{},(),set(),False])
True
>>> len(l)
4
>>> #membership operation of list
>>> l
[7, 45, 4, 7]
>>> 7 in l
True
>>> 5 in l
False
>>> 
>>> 7 not in l
False
>>> 5 not in l
True
>>> l=[5,7,9,43,54]
>>> l.index(7)
1
>>> l.index(77)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    l.index(77)
ValueError: 77 is not in list
>>> l.count(43)
1
>>> l.count(1)
0
>>> l=[[3,67,89,79],[23,1,45,24]]
>>> l[0][3]
79
>>> l[1][-1]
24
>>> l[1][3]
24
>>> t=tuple()
>>> t
()
>>> t=(7,'str',12.3,1+3j,[45,'tuple'],{0,1,7},(65,78))
>>> t
(7, 'str', 12.3, (1+3j), [45, 'tuple'], {0, 1, 7}, (65, 78))
>>> t=(1,1,7,89,5,5,54)
>>> t
(1, 1, 7, 89, 5, 5, 54)
