>>> s =""
>>> 
>>> s
''
>>> s ="codegnan"
>>> s
'codegnan'
>>> "codegnan"+"PFS"
'codegnanPFS'
>>> "codegnan"*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
>>> "_*_"*10
'_*__*__*__*__*__*__*__*__*__*_'
>>> names = "Shruti Divya Sri"
>>> names
'Shruti Divya Sri'
>>> names[0]
'S'
>>> #indexing
>>> names[7]
'D'
>>> #slicing
>>> names[0:7]
'Shruti '
>>> names[:6]
'Shruti'
>>> names[7:]
'Divya Sri'
>>> #slicing with skip value
>>> names[2::2]
'rt iy r'
>>> names[2:-1:2]
'rt iy r'
>>> names[2:15:2]
'rt iy r'
>>> names[0:-1:-1]
''
>>> names[0:-1:-2]
''
>>> names[-1:-14:-1]
'irS ayviD itu'
>>> 