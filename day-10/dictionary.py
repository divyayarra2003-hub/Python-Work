data= {'name':'sri', 'batch':63, 'course':'PFS'}
data
{'name': 'sri', 'batch': 63, 'course': 'PFS'}
id(data)
2756628761600
data['name']
'sri'
data['batch']
63
data['course']
'PFS'
'course' in data
True
63 in data
False
data.get('name','key is not found')
'sri'
data.get(1,"key is not found")
'key is not found'
data['batch'] = 64
data
{'name': 'sri', 'batch': 64, 'course': 'PFS'}
data['skills'] = ['python', 'mysql', 'flask']
data
{'name': 'sri', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data.update({'rank':1, 'branch':5, 'email':'sri@gmail.com'})
data
{'name': 'sri', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5, 'email': 'sri@gmail.com'}
data.pop()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
data.pop('batch')
64
data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5, 'email': 'sri@gmail.com'}
data.pop('email')
'sri@gmail.com'
data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5}
data.popitem()
('branch', 5)
data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1}
del data.rank
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    del data.rank
AttributeError: 'dict' object has no attribute 'rank' and no __dict__ for setting new attributes
del data['rank']
data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data.clear()
data
{}
data = {'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5, 'email': 'sri@gmail.com'}
data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5, 'email': 'sri@gmail.com'}
data.keys()
dict_keys(['name', 'course', 'skills', 'rank', 'branch', 'email'])
data.values()
dict_values(['sri', 'PFS', ['python', 'mysql', 'flask'], 1, 5, 'sri@gmail.com'])
data.items()
dict_items([('name', 'sri'), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('rank', 1), ('branch', 5), ('email', 'sri@gmail.com')])
sorted(data)
['branch', 'course', 'email', 'name', 'rank', 'skills']
sorted(data, reverse=True)
['skills', 'rank', 'name', 'email', 'course', 'branch']
max(data)
'skills'
min(data)
'branch'
data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5, 'email': 'sri@gmail.com'}
data['age']
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    data['age']
KeyError: 'age'
>>> data.get('age')
>>> data.get('age','key not found')
'key not found'
>>> data.setdefault('age',0)
0
>>> data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5, 'email': 'sri@gmail.com', 'age': 0}
>>> data.setdefault('name','')
'sri'
>>> data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5, 'email': 'sri@gmail.com', 'age': 0}
>>> len(data)
7
>>> all(data)
True
>>> any(data)
True
>>> data
{'name': 'sri', 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'rank': 1, 'branch': 5, 'email': 'sri@gmail.com', 'age': 0}
>>> a={1:1,2:2}
>>> b=a
>>> b[3]=3
>>> b
{1: 1, 2: 2, 3: 3}
>>> a
{1: 1, 2: 2, 3: 3}
>>> c=a.copy()
>>> c[4]=4
>>> c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3}
>>> d = dict.fromkeys(['a','b'],0)
>>> d
{'a': 0, 'b': 0}