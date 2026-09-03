x = input("enter a value")
enter a value4
x
'4'
y = int(input("enter a value"))
enter a value4
y
4
type(x)
<class 'str'>
type(y)
<class 'int'>
names = input("enter the names ")
enter the names sri divya shruti
names
'sri divya shruti'
list(names.split())
['sri', 'divya', 'shruti']
tuple(names.split())
('sri', 'divya', 'shruti')
>>> set(names.split())
{'divya', 'shruti', 'sri'}
>>> names2 = list(input("enter the names: ").split())
enter the names: sri divya sruthi
>>> names2
['sri', 'divya', 'sruthi']
>>> values = list(map(int, input("enter the numbers: ").split()))
enter the numbers: 67 89 90 80
>>> values
[67, 89, 90, 80]
>>> tuple(map(int, values.split()))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(map(int, values.split()))
AttributeError: 'list' object has no attribute 'split'
>>> tuple(values)
(67, 89, 90, 80)
>>> set(values)
{80, 89, 90, 67}
>>> nums = list(map(float,input("enter the numbers: ").split()))
enter the numbers: 785 85438 49398 85439
>>> nums
[785.0, 85438.0, 49398.0, 85439.0]
>>> tuple(nums)
(785.0, 85438.0, 49398.0, 85439.0)
>>> set(nums)
{85439.0, 785.0, 85438.0, 49398.0}
>>> email, password = list(input("enter your email and password: ").split())
enter your email and password: something@gmail.com something@
>>> email
'something@gmail.com'
>>> password
'something@'
>>> #eval
>>> e = eval(input())
"divya"
>>> e
'divya'
>>> e=eval(input())
{1:1, 2:2, 3:3}
>>> e
{1: 1, 2: 2, 3: 3}
>>> e=eval(input())
2+3*4+5*8
>>> e
54