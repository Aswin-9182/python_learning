Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> e='''course'''
>>> type(e)
<class 'str'>
>>> f=4+9j
>>> type(f)
<class 'complex'>
>>> g=2j+8
>>> type(g)
<class 'complex'>
>>> i=7j
>>> type(i)
<class 'complex'>
>>> k=9i
SyntaxError: invalid decimal literal
>>> l=j
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l=j
NameError: name 'j' is not defined
>>> m="j
SyntaxError: unterminated string literal (detected at line 1)
>>> m="j"
>>> type(m)
<class 'str'>
>>> x=True
>>> type(x)
<class 'bool'>
>>> y=False
>>> typr(y)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    typr(y)
NameError: name 'typr' is not defined. Did you mean: 'type'?
>>> type(f)
<class 'complex'>
>>> type(y)
<class 'bool'>
>>> z=true
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    z=true
NameError: name 'true' is not defined. Did you mean: 'True'?
z="true"
type(z)
<class 'str'>
#datatype conversions
#int
int(3)
3
int("string")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    int("string")
ValueError: invalid literal for int() with base 10: 'string'
int(2.5)
2
int(2+5j)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(2+5j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(2)
2.0
float(30.4)
30.4
float("string")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    float("string")
ValueError: could not convert string to float: 'string'
float(2+5j)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(2+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
String(1)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    String(1)
NameError: name 'String' is not defined
string(1)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    string(1)
NameError: name 'string' is not defined. Did you forget to import 'string'?
str(1)
'1'
str(2.5)
'2.5'
str(3+4j)
'(3+4j)'
str(True)
'True'
str(False)
'False'
complex(1)
(1+0j)
complex(3+6j)
(3+6j)
complex("string")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex("string")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
complex(4.6)
(4.6+0j)
bool(1)
True
bool(3.5)
True
bool(3+2j)
True
bool(True)
True
bool(False)
False
