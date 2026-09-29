Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List
>>> a=[2,4.4,'python',3+4j,True,False]
>>> print(a)
[2, 4.4, 'python', (3+4j), True, False]
>>> type(a)
<class 'list'>
>>> b=True
>>> print(b)
True
>>> c=[True]
>>> type(c)
<class 'list'>
>>> #append
>>> a=['python','java']
>>> a.append('c')
>>> a
['python', 'java', 'c']
>>> a.append(['ml','c++'])
>>> a
['python', 'java', 'c', ['ml', 'c++']]
>>> #Extend
>>> b=['python', 'java']
>>> b.extend(['ml','c'])
>>> b
['python', 'java', 'ml', 'c']
>>> #Insert
>>> c=['python','java']
>>> c.insert(1,'ds')
>>> c
['python', 'ds', 'java']
>>> #index
>>> a=['hyd','vij','vzg']
>>> a.index('vij')
1
>>> #copy
>>> a=['hyd','vij','vzg']
>>> b=a.copy()
>>> b
['hyd', 'vij', 'vzg']
>>> #sort
>>> a=['mango','banana','grapes','apple']
>>> a.sort()
>>> a
['apple', 'banana', 'grapes', 'mango']
>>> b=[4,23,4,2,6,8]
b.sort()
b
[2, 4, 4, 6, 8, 23]
a=['Mango','banana','Grapes','apple','Banana']
a.sort()
a
['Banana', 'Grapes', 'Mango', 'apple', 'banana']
#Reverse
a=['black','red','green']
a.reverse()
a
['green', 'red', 'black']
b=[2,6,3,7,6]
a.reverse()
a
['black', 'red', 'green']
b
[2, 6, 3, 7, 6]
b.reverse()
b
[6, 7, 3, 6, 2]
#pop
a=['java','ds','ai']
a.pop()
'ai'
a
['java', 'ds']
#remove
a.remove()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
c=['java','ds','ai']
c.remove()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    c.remove()
TypeError: list.remove() takes exactly one argument (0 given)
c.remove('ds')
c
['java', 'ai']
#clear
c.clear()
c
[]
c.append(['html'])
c
[['html']]
#len
a=['hi','hello']
len(a)
2
a.count()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
a.count('hi)
        
SyntaxError: incomplete input
a.count('hi')
        
1
