d ={}
type(d)
<class 'dict'>
d = dict()
type(D)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(D)
NameError: name 'D' is not defined. Did you mean: 'd'?
type(d)
<class 'dict'>

d ={'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
1641007073152
d['k4'] ='v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
id(d)
1641007073152
d['k1'] = 'v11'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d[1]='int'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int'}
d[2.7]='flt'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 2.7: 'flt'}
d[2+7j] = 'cmplx'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 2.7: 'flt', (2+7j): 'cmplx'}
d['s'] ='str'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 2.7: 'flt', (2+7j): 'cmplx', 's': 'str'}
d[[1,2,3]] = 'list'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    d[[1,2,3]] = 'list'
TypeError: unhashable type: 'list'
d[(1,'str')]='set'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 2.7: 'flt', (2+7j): 'cmplx', 's': 'str', (1, 'str'): 'set'}
d[(1,'str')]='tuple'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 2.7: 'flt', (2+7j): 'cmplx', 's': 'str', (1, 'str'): 'tuple'}
d[{1,2}]='set'
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d[{1,2}]='set'
TypeError: unhashable type: 'set'
d[{'int':1}] ='dict'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d[{'int':1}] ='dict'
TypeError: unhashable type: 'dict'
d[frozenset({1,7})]='frozenset'
d
{'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 1: 'int', 2.7: 'flt', (2+7j): 'cmplx', 's': 'str', (1, 'str'): 'tuple', frozenset({1, 7}): 'frozenset'}
d={}
d
{}
d[1]=1
d[2]=2.7
d[3]=5+7j
d[4]='string'
d[5]=[1,"string"]
d[6]=(7,"tuple")
d[7]={1,2,3,'tuple'}
d[8]=frozenset({3,4})
d[9]={'key':'value',3+9j:'complex'}
d
{1: 1, 2: 2.7, 3: (5+7j), 4: 'string', 5: [1, 'string'], 6: (7, 'tuple'), 7: {1, 2, 3, 'tuple'}, 8: frozenset({3, 4}), 9: {'key': 'value', (3+9j): 'complex'}}
>>> d[9]={'key':'value',3+ij:'complex'}
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    d[9]={'key':'value',3+ij:'complex'}
NameError: name 'ij' is not defined. Did you mean: 'id'?
>>> d
{1: 1, 2: 2.7, 3: (5+7j), 4: 'string', 5: [1, 'string'], 6: (7, 'tuple'), 7: {1, 2, 3, 'tuple'}, 8: frozenset({3, 4}), 9: {'key': 'value', (3+9j): 'complex'}}
>>> id(d)
1641014017216
>>> 
>>> 9 in d
True
>>> 10 in d
False
>>> 
>>> 'str' in d
False
>>> d[5]
[1, 'string']
>>> d[8]
frozenset({3, 4})
>>> d[10]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    d[10]
KeyError: 10
>>> d.get(10)
>>> d.get(1)
1
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(7,"key is not present")
{1, 2, 3, 'tuple'}
>>> d.keys()
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> d.values()
dict_values([1, 2.7, (5+7j), 'string', [1, 'string'], (7, 'tuple'), {1, 2, 3, 'tuple'}, frozenset({3, 4}), {'key': 'value', (3+9j): 'complex'}])
>>> d.items()
dict_items([(1, 1), (2, 2.7), (3, (5+7j)), (4, 'string'), (5, [1, 'string']), (6, (7, 'tuple')), (7, {1, 2, 3, 'tuple'}), (8, frozenset({3, 4})), (9, {'key': 'value', (3+9j): 'complex'})])
>>> d[6] = 12
>>> d
{1: 1, 2: 2.7, 3: (5+7j), 4: 'string', 5: [1, 'string'], 6: 12, 7: {1, 2, 3, 'tuple'}, 8: frozenset({3, 4}), 9: {'key': 'value', (3+9j): 'complex'}}
>>> d[7]=20
>>> d
{1: 1, 2: 2.7, 3: (5+7j), 4: 'string', 5: [1, 'string'], 6: 12, 7: 20, 8: frozenset({3, 4}), 9: {'key': 'value', (3+9j): 'complex'}}