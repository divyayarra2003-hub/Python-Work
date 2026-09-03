a = set()
a
set()
a.add(1)
a.add(7.5)
a.add("string")
a.add(7+5j)
a.add([2,3,5])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.add([2,3,5])
TypeError: unhashable type: 'list'
a.add(("k",2))
a.add({1,1})
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.add({1,1})
TypeError: unhashable type: 'set'
a.add({"d":"dictionary"})
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a.add({"d":"dictionary"})
TypeError: unhashable type: 'dict'
a = {1,2,3,4,5}
b = {3,5,7,9}
type(a)
<class 'set'>
#we can operate set in 2 types (all the operations)
a+b
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a*b
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a*b
TypeError: unsupported operand type(s) for *: 'set' and 'set'
a[1]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a[1]
TypeError: 'set' object is not subscriptable
5 in a
True
a|b
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
a<=b
False
a>=b
False
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
# or else we can operate the same above elements like this also
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.difference(b)
{1, 2, 4}
a.symmetric(b)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.symmetric(b)
AttributeError: 'set' object has no attribute 'symmetric'

{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{1,2,3,4,5}<=a
True
{1,2,3,4,5,6}<=a
False
b
{9, 3, 5, 7}
a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint(b)
False
a.issubset(b)
False
a.isdisjoint({9,10})
True
a.issuperset(b)
False
s = {1,2,3,4,5,6,7,8,9}
s
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.issuperset(b)
False
s.issuperset(b)
True
b.issubset(s)
True

max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(17)
b
{1, 2, 3, 4, 5, 17}
a
{1, 2, 3, 4, 5, 17}
c=a.copy()
c.add(7)
c
{1, 2, 3, 4, 5, 17, 7}
a
{1, 2, 3, 4, 5, 17}
a.add(123)
a
{1, 2, 3, 4, 5, 17, 123}
a.update({16,17,18})
a
{1, 2, 3, 4, 5, 16, 17, 18, 123}
a.pop(16)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.pop(16)
TypeError: set.pop() takes no arguments (1 given)
a.pop()
1
>>> a.remove(16)
>>> a
{2, 3, 4, 5, 17, 18, 123}
>>> a.remove(16)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.remove(16)
KeyError: 16
>>> a.discard(16)
>>> a
{2, 3, 4, 5, 17, 18, 123}
>>> a.discard(2)
>>> a
{3, 4, 5, 17, 18, 123}
>>> a.clear()
>>> a
set()
>>> len(s)
9
>>> all(a)
True
>>> any(a)
False
>>> 

>>> 

... 
>>> a = frozenset({1,13,14,56,79})
>>> a
frozenset({1, 56, 13, 14, 79})
>>> type(a)
<class 'frozenset'>
>>> a.add(99)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.add(99)
AttributeError: 'frozenset' object has no attribute 'add'