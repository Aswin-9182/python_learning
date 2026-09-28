Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string methods
a='Python'
len(a)
6
b='python course'
len(a)
6
c=""
len(a)
6
len(c)
0
d=" "
len(d)
1
#count
a='classmate'
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("mate")
1
a.count("s")
2
#find a string
a=python
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a=python
NameError: name 'python' is not defined
a='python'
a.find('t')
2
a.find('a')
-1
#escape sequences
#\n-> new line
#\t-? tab space
a='name\nmobileno\tcollege\nmailid\tbranch'
print(a)
name
mobileno	college
mailid	branch
a='name:Aswin\nmobileno:918234213\tcollege: TKRC\nmailid: aswin@gmail.com\tbranch: IT'
print(a)
name:Aswin
mobileno:918234213	college: TKRC
mailid: aswin@gmail.com	branch: IT
#Repalce
a='wait until you succeed'
a.replace('wait','work')
'work until you succeed'
print(a)
wait until you succeed
#upper case
a='python'
a.upper()
'PYTHON'
a='PYTHON'
a.lower()
'python'
#capitalize
a='mobile number'
a.capitalize()
'Mobile number'
#Title
a='i am in class'
a.title()
'I Am In Class'
#conditions
a='aswin'
a.islower()
True
a.isupper()
False
b='ASWIN'
b.isupper()
True
c='data science'
c.endswith()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    c.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
c.endswith('d')
False
c.startwith('d')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    c.startwith('d')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
c.startswith('d')
True
a='123'
a.isnum()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
a.isalnum()
True
e='123'
e.isalnum()
True
f='asw12'
f.isdigit()
False
g='asW'
g.isalfa()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    g.isalfa()
AttributeError: 'str' object has no attribute 'isalfa'. Did you mean: 'isalpha'?
g.isalpha()
True
#strip
#lstrip , rstrip
a='    aswin  '
a.strip()
'aswin'
a.lstrip()
'aswin  '
a.rstrip()
'    aswin'
#concatanation
a='code'
b='gnan'
print(a+b)
codegnan
print(a+' '+b)
code gnan
fname='aswin'
lname='g'
print(fname+' '+lname)
aswin g
print(fname.title()+' '+lname.title())
Aswin G
#Real use case method
print((fname+' '+lname).title())
Aswin G
#split
a='c python java'
a.split()
['c', 'python', 'java']
a.split(' ')
['c', 'python', 'java']
>>> #join
>>> a='apple','banana','grapes'
>>> ''.join(a)
'applebananagrapes'
>>> ' '.join(a)
'apple banana grapes'
>>> #formating
>>> # adding additional data
>>> a=3
>>> b=10
>>> print(a+b)
13
>>> print('the sum is',a+b)
the sum is 13
>>> city='Khammam'
>>> print('city is',city)
city is Khammam
>>> #format method
>>> a='motu'
>>> b='patlu'
>>> print('hello {} {}',format(a,b))
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print('hello {} {}',format(a,b))
ValueError: Invalid format specifier 'patlu' for object of type 'str'
>>> print('hello {} {}'.format(a,b))
hello motu patlu
>>> print('hello {}, hello {}'.format(a,b))
hello motu, hello patlu
>>> print('hello {}, hello {}'.format(a,b).title())
Hello Motu, Hello Patlu
>>> #fstring
>>> a='aswin'
>>> b='g'
>>> print(f'hello {a} {b}')
hello aswin g
>>> print(f'hello {a} {b}'.title())
Hello Aswin G
>>> 
>>> a=3
>>> b=5
>>> mul=a*b
>>> print(f'multiplication of {a} and {b} is {mul}')
multiplication of 3 and 5 is 15
>>> print('multiplication of {} and{} is {}'.format(a,b,mul))
multiplication of 3 and5 is 15
