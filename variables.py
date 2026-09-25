Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
print(4+8)
12
a=10
print(a)
10
x=50
print(x)
50
print(X)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
z=100
print(z)
100
3=90
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3=90
print(a3)
90
5x=9
SyntaxError: invalid decimal literal
a0123456789=100
print(a0123456789)
100
name="pooja"
print(name)
pooja
print("name")
name
city="vja"
print(city)
vja
country="india"
print(country)
india
a=8
b=9
print(a+b)
17
fname="pooja"
lname="ch"
print(fname+lname)
poojach
print(fname+" "+lname)
pooja ch
a=3,b=7
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=3;b=9
print(a+b)
12
a,b=6,7
print(a+b)
13
a=4
b=8
print(a+b)
12
@=9
SyntaxError: invalid syntax
$=9
SyntaxError: invalid syntax
_=40
print(_)
40
_a=100
print(_a)
100
if=20
SyntaxError: invalid syntax
while=20
SyntaxError: invalid syntax
a=2,3,4,5,6,7,8,9)
SyntaxError: unmatched ')'
a=(2,3,4,5,6,7,8,9)
print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
a,b,c=2,3,4
print(a,b,c)
2 3 4
first name="pooja"
SyntaxError: invalid syntax
first_name="pooja"
print(first_name)
pooja
>>> firstname="pooja"
>>> print(firstname)
pooja
>>>  a=3
...  
SyntaxError: unexpected indent
>>> _a=9
>>> print(-a)
-2
>>> print(a)
2
>>> print(_a)
9
>>> a=(1,2,3)
>>> print(a)
(1, 2, 3)
>>> a,b,c=(5,6,7)
>>> print(a,b,c)
5 6 7
>>> a=90
>>> print(a)
90
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
>>> name="pooja"
>>> print(name)
pooja
>>> Name="pooja"
>>> print(Name)
pooja
>>> NAME="pooja"
>>> print(NAME)
pooja
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> a=b=c=10
>>> print(a,b,c)
10 10 10
