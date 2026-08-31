Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=10
a+b
30
a-b
10
a+b
30
a*b
200
a/b
2.0
a//b
2
a%b
0

a**b
10240000000000
a>b
True
a<b
False
a==b
False
a>=b
True
a<=b
False
a!=b
True
c=10
c
10
c = c+10
c
20
c+=10
c
30
c-=5
c
25
c//=5
c
5
c*=2
c
10
c%=2
c
0
c=30
c/=15
c
2.0
c**=2
c
4.0
c//=c
c
1.0
c//=1
c
1.0
n=10
n
10
n%2==0
True
n%3==0
False
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%8==0 or n%3==0
False
n<5
False
!n<5
SyntaxError: invalid syntax
not n<5
True
s ="codegnan"
"e" in s
True
"z" in s
False
"f" in s
False
"f" not in s
True
l = [4,6,7,9]
7 in l
True
10 not in l
True
t = (4,7,9,1)
1 in t
True
5 in t
False
10 not in t
True
s3 = {2,"sri",77}
sri in s3
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    sri in s3
NameError: name 'sri' is not defined
"sri" in s3
True
5 not in s3
True
d = {"name":"codegnan","batch":5,"course":"pfs"}
d
{'name': 'codegnan', 'batch': 5, 'course': 'pfs'}
name in d
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
"name" in d
True
"codegnan" in d
False
"batch" in d
True
5 in d
False
# membership operators work for key only
#arithmetic operators: +,-,*,/,//,%,**
#assignment operators: =,+=,-=,*=,/=,//=,%=,**=
#comparision operators: >,<,>=,<=,==,!=
#relational operators: and, or, not
#membership operators: in, not in
#identity operators: is, is not
#identity operators check whether the elements are sharing the same memory reference
l=[4,6,9,8]
m=[4,6,9,8]
id(l)
1301745457984
id(m)
1301745071104
l is m
False
m is l
False
n = l
l is n
True
#list, set, dictionary
#these are mutable, mutable means even when we change the values within the sequence, the memory location remains same
#bitwise operators &,|,^,>>,<<
9&10
8
9|10
11
9^10
3
>>> 9>>10
0
>>> 9<<10
9216
>>> 

>>> a=10
>>> b=10.3
>>> c="codegnan"
>>> print(a,b,c)
10 10.3 codegnan
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"| b value is",b,"| c value is",c)
a value is 10 | b value is 10.3 | c value is codegnan
>>> print(a,b,c)
10 10.3 codegnan
>>> print(a,b,c,sep="")
1010.3codegnan
>>> print(a,b,c,sep="\n")
10
10.3
codegnan
>>> print(a,b,c,sep="\t")
10	10.3	codegnan
>>> print(a,b,c,sep="\t",end="@")
10	10.3	codegnan@
>>> print(a,b,c,sep="\t",end="\n\n")
10	10.3	codegnan

>>> 
>>> #fstring
>>> print(f"a={a} b={b} c={c}")
a=10 b=10.3 c=codegnan
>>> print("a=%d b=%f c=%s"%(a,b,c))
a=10 b=10.300000 c=codegnan
>>> print("a=%d b=%.2f c=%s"%(a,b,c))
a=10 b=10.30 c=codegnan
>>> print("a={} | b={} | c={}".format(a,b,c))
a=10 | b=10.3 | c=codegnan
>>> print("a={} | b={} | c={}".format(c,a,b))
a=codegnan | b=10 | c=10.3
>>> print("a={1} | b={2} | c={0}".format(a,b,c))
a=10.3 | b=codegnan | c=10
>>> print(f"a value is {a}| b value is {b} | c value is {c}")
a value is 10| b value is 10.3 | c value is codegnan
