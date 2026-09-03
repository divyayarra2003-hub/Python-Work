c ="python programming"
c
'python programming'
len(c)
18
ord(c)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ord(c)
TypeError: ord() expected a character, but string of length 18 found
ord("p")
112
ord("a")
97
chr(66)
'B'
chr(12)
'\x0c'
chr(50)
'2'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
s = "string is immutable"
s
'string is immutable'
s.upper()
'STRING IS IMMUTABLE'
s.lower()
'string is immutable'
s.capitalize()
'String is immutable'
s.title()
'String Is Immutable'
s.swapcase()
'STRING IS IMMUTABLE'
"STRAẞEMÁLAGAÅngströmCafé".casefold()
'strassemálagaångströmcafé'

c.center(0,"_")
'python programming'
c.center(70,"_")
'__________________________python programming__________________________'
c.center(50,"*")
'****************python programming****************'
c.rjust(70,"-")
'----------------------------------------------------python programming'
c.ljust(70,"-")
'python programming----------------------------------------------------'
"17".zfill(4)
'0017'
"st".zfill(7)
'00000st'

c
'python programming'
c.find("o")
4
c.rfind("o")
9
c.find("z")
-1
c.index("o")
4
c.index("z")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    c.index("z")
ValueError: substring not found
c.count("p")
2
c.count("g")
2
c.count("y")
1
c.count("d")
0
c.rindex("o")
9
c.rfind("on")
4
c.count("on")
1
c.replace("i","s")
'python programmsng'
c.replace("programming","coding")
'python coding'
c.maketrans("aeiou","12345")
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.translate(c.maketrans("aeiou","12345"))
'pyth4n pr4gr1mm3ng'
c.translate(c.maketrans("aeiou","*****"))
'pyth*n pr*gr*mm*ng'

s
'string is immutable'
s.split()
['string', 'is', 'immutable']
s.split(",")
['string is immutable']
s.split("-")
['string is immutable']
"string is immutable".split("-")
['string is immutable']
"string is immutable".split(",")
['string is immutable']
"string is immutable".split()
['string', 'is', 'immutable']
"string is immutable".rsplit()
['string', 'is', 'immutable']
s
'string is immutable'
s.splitlines()
['string is immutable']
s ="""
python
programming language"""
s
'\npython\nprogramming language'
s.splitlines()
['', 'python', 'programming language']
s='''
python
programming
language'''
s.splitlines()
['', 'python', 'programming', 'language']
['', 'python', 'programming', 'language'].join()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    ['', 'python', 'programming', 'language'].join()
AttributeError: 'list' object has no attribute 'join'
"".join(['', 'python', 'programming', 'language'])
'pythonprogramminglanguage'
" ".join(s)
'\n p y t h o n \n p r o g r a m m i n g \n l a n g u a g e'
>>> "--".join(['', 'python', 'programming', 'language'])
'--python--programming--language'
>>> s ="python,c,c++,java,javascript"
>>> s
'python,c,c++,java,javascript'
>>> s.partition(',')
('python', ',', 'c,c++,java,javascript')
>>> s.rpartition(',')
('python,c,c++,java', ',', 'javascript')
>>> #split divides the entire string, partition divides the string into 3 parts
>>> s.rpartition('-')
('', '', 'python,c,c++,java,javascript')
>>> c = '        python programming                   '
>>> c
'        python programming                   '
>>> c.strip()
'python programming'
>>> c.lstrip()
'python programming                   '
>>> c.rstrip()
'        python programming'
>>> s = '-----------string concept----------'
>>> s.strip('-')
'string concept'
>>> s.lstrip('-')
'string concept----------'
>>> s.rstrip('-')
'-----------string concept'
>>> s = '----string -- concept----'
>>> s
'----string -- concept----'
>>> s.strip('-')
'string -- concept'
>>> text = "Hello नमस्ते你好 café 🙂"
>>> text
'Hello नमस्ते你好 café 🙂'
>>> text.encode()
b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'
>>> text.decode()
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    text.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
>>> b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'.decode()
'Hello नमस्ते你好 café 🙂'