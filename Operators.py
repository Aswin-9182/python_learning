Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Arithematic
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a/b)
0.5
print(a//b)
0
print(a**b)
16
print(a%b)
2
# Assignment
a=4
b=6
a+=b
a
10
b+=a
b
16
b-=a
b
6
b*=a
b
60
b//=a
b
6
b/=a
b
0.6
b%=a
b
0.6
a
10
# Comparision
a=5
b=8
a<b
True
a>b
False
b<a
False
b>a
True
a<=b
True
a>=b
False
a!=b
True
a==b
False
a=4
b=4
a==b
True
# Logical
a=10
b=20
a<b and a>b
False
a<b and b>a
True
a!=b and a==b
False
a<b or b>a
True
a!=b or a==b
True
not False
True
not True
False
a=5
type(a) is int
True
type(a) is not in
SyntaxError: incomplete input
type(a) is not int
False
type(a) is not float
True
b=4.2
type(b) is float
True
type(b) is not float
False
type(b) is not int
True
a=2+4j
type(a) is complex
True
type(a) is not complex
False
a=True
type(a) is bool
True
type(a) is not bool
False
# Membership
a=4,5,6,7,8
6 in a
True
10 in a
False
>>> 10 not in a
True
>>> 4 not in a
False
>>> # Bitwise
>>> a=4
>>> b=6
>>> a&b
4
>>> bin(4)
'0b100'
>>> bin(6)
'0b110'
>>> 
>>> a=5
>>> b=7
>>> a|b
7
>>> a=2
>>> b=4
>>> a|b
6
>>> a=5
>>> -(a+1)
-6
>>> ~a
-6
>>> a=-6
>>> ~a
5
>>> -(a+1)
5
>>> a=5
>>> b=9
>>> a^b
12
>>> a=4
>>> a<<2
16
>>> a=8
>>> a<<3
64
>>> a=6
>>> a>>2
1
