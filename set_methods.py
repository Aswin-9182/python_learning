Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #sets
>>> a={4,2.6,'python',True,False}
>>> 
>>> print(a)
{False, True, 2.6, 4, 'python'}
>>> type(a)
<class 'set'>
>>> #add
>>> a={4,5,6,7,8,9}
>>> a.add(10)
>>> a
{4, 5, 6, 7, 8, 9, 10}
>>> a={2,3,4,5}
>>> b={4,5,6,7}
>>> b.issubset(a)
False
>>> a.issubset(b)
False
>>> a={3,4,5,6,7,8}
>>> b={5,6,7,8}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> a={2,3,4,5,6,7}
>>> b={4,5,6}
>>> a.issuperset(b)
True
>>> b.issuperset(a)
False
>>> #union
>>> a={2,3,4,5,6}
>>> b={5,6,7,8}
>>> a.union(b)
{2, 3, 4, 5, 6, 7, 8}
>>> a
{2, 3, 4, 5, 6}
>>> #intresection
>>> a={1,2,3,4,5}
>>> b={4,5,6,7,8}
>>> a.intersection(b)
{4, 5}
>>> #update
>>> a={2,3,4,5,6}
>>> b={5,6,7,8,9}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9}
b
{5, 6, 7, 8, 9}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
#differrence
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.difference(b)
{8, 5, 6, 7}
b.difference(a)
{12, 13, 14}
#symmetric difference
#it delets same elements and print
a={3,4,5,6,7,8}
b=5,6,7,8,9,10}
SyntaxError: unmatched '}'
b={5,6,7,8,9,10}
a.symmetric_difference(b)
{3, 4, 9, 10}

#difference update
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.difference_update(b)
a
{4, 5}
b.difference_update(a)
b
{6, 7, 8, 9, 10, 11}
a={5,6,7,8,9,10,11}
b={9,10,11,12,13,14}
a.intersection_update(b)
a
{9, 10, 11}
b.intersection_update(a)
b
{9, 10, 11}
a.a={10,20,30,40,50}
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.a={10,20,30,40,50}
AttributeError: 'set' object has no attribute 'a'
a={10,20,30,40,50}
b={30,40,50,60,70}
a.symmetric_difference_update(b)
a
{20, 70, 10, 60}
b.symmetric_difference_update(a)
b
{50, 20, 40, 10, 30}
#pop
a={2,3,4,5,6,7}
a.pop()
2
a
{3, 4, 5, 6, 7}
a.remove(5)
a
{3, 4, 6, 7}
a={5,6,7,8,9,10}
a.copy()
{5, 6, 7, 8, 9, 10}
a.clear()
a
set()
b=set()
b.add(50)
b
{50}
#disjoint
a={4,5,6,7,8}
b={9,10,11,12}
a.isdisjoint(b)
True
#len
a={2,3,4,5,6}
len(a)
5
