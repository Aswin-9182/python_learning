Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dictionary
>>> a={'naame':'Aswin','year':2026,'month':9}
>>> print(a)
{'naame': 'Aswin', 'year': 2026, 'month': 9}
>>> type(a)
<class 'dict'>
>>> b={'name','year','month'}
>>> b
{'year', 'name', 'month'}
>>> type(b)
<class 'set'>
>>> a.keys()
dict_keys(['naame', 'year', 'month'])
>>> a.values()
dict_values(['Aswin', 2026, 9])
>>> a.items()
dict_items([('naame', 'Aswin'), ('year', 2026), ('month', 9)])
>>> a={'name':'aswin','city':'vij'}
>>> 
>>> a['name']
'aswin'
>>> a.get('aswin}
...       
SyntaxError: incomplete input
>>> a.get('aswin')
...       
>>> a
...       
{'name': 'aswin', 'city': 'vij'}
>>> a['aswin']
...       
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a['aswin']
KeyError: 'aswin'
>>> a={'city':'vij','state':'ap','country':'india'}
...       
>>> a.pop()
...       
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop('state')
...       
'ap'
a.popitem()
      
('country', 'india')
a
      
{'city': 'vij'}
a={'coure':'python','duration':100}
      
a={'coure':'python','duration':100}
      
a.update({'year':2026})
      
a
      
{'coure': 'python', 'duration': 100, 'year': 2026}
a.update({'month':'sep'},{'date':30})
      
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.update({'month':'sep'},{'date':30})
TypeError: update expected at most 1 argument, got 2
a.update({'month':'sep','date':30})
      
a
      
{'coure': 'python', 'duration': 100, 'year': 2026, 'month': 'sep', 'date': 30}
#Set default
      
a={'date':30,'time':11}
      
a.setdefault('hour',11)
      
11
a
      
{'date': 30, 'time': 11, 'hour': 11}
a={'colour':'white','food':'biryani'}
      
a.copy()
      
{'colour': 'white', 'food': 'biryani'}
len(a)
      
2
a.count()
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a.index()
      
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.index()
AttributeError: 'dict' object has no attribute 'index'
a.clear()
      
a
      
{}
a={'name':"Aswin",'city':'vij','name':'Aswin'}
      
a
      
{'name': 'Aswin', 'city': 'vij'}

a={'name':"Aswin",'city':'vij','name':'Arjun'}
      
a
      
{'name': 'Arjun', 'city': 'vij'}
a={'name1':"Aswin",'city':'vij','name2':'Aswin'}
      
a
      
{'name1': 'Aswin', 'city': 'vij', 'name2': 'Aswin'}
a={'idnos':10,20,30}
      
SyntaxError: ':' expected after dictionary key
a={'idnos':[10,20,30],'names':['aswin','kiran','suresh']}
      
type(a)
      
<class 'dict'>
a.keys()
      
dict_keys(['idnos', 'names'])
a.values()
      
dict_values([[10, 20, 30], ['aswin', 'kiran', 'suresh']])
a.items()
      
dict_items([('idnos', [10, 20, 30]), ('names', ['aswin', 'kiran', 'suresh'])])
