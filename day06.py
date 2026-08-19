#SET METHODS
#create a empty dict and print its type
d={}
print(type(d))   #class is dict
#create a empty set and print its type
a=set()
print(type(a))    #class is set
#add 5 non-sequences and 5 sequences to that set with add method
a= set()
a.add(2)
a.add(5.3)
a.add(3+4j)
a.add(True)
a.add(None)
print(a)
#a.add([1,2,3])     error because list is mutable
a.add((1,2,3))
#a.add({1: 'a', 2: 'b'})   error, dict mutable
a.add('aswin')
a.add(range(1,4))
#a.add({1,2,3})       Error, set is mutable
print(a)
#add 5 non-sequences and 5 sequences with update method
a= set()
#a.update(2)        error, only sequence element
#a.update(5.3)      error, only sequence element
#a.update(3+4j)     error, only sequence element
#a.update(True)     error, only sequence element
#a.update(None)     error, only sequence element
print(a)
a.update([1,2,3]) 
a.update((1,2,3))
a.update({1: 'a', 2: 'b'})
a.update('aswin')
a.update(range(1,4))
a.update({1,2,3})
print(a)

#print a set and remove first element from that set
a={1, 2 , 3, 5}
print(a)
a.pop()
print(a)
#remove one existing and one non-existing element from that set
a.remove(3)
print(a)
#a.remove(7)   Error, there is no element in the set
#discard one existing and one non-existing element from that set
a.discard(2)
a.discard(6)    # if it is not in set no changes the set
print(a)
#remove all elements from the set
a.clear()
print(a)

#create a set {1,2,3,4}, a list [3,4,5,6]. 
s={1,2,3,4}
l=[3,4,5,6]
#write union of set and list
print(s.union(l))
#write intersection of set and list
print(s.intersection(l))
#write difference of set and list
print(s.difference(l))
#write symmetric difference of set and list
print(s.symmetric_difference(l))

#use union, intersection, difference, symmetric difference operators on set and another set. try to change second type of list and see outputs
s={1,2,3,4}
l={3,4,5,6}
print(s|l)
print(s&l)
print(s-l)
print(s^l)

s={1,2,3,4}
l=[3,4,5,6]
#print(s|l) cannot add set and list
#print(s&l)  cannot add set and list
#print(s-l)  cannot add set and list
#print(s^l)  cannot add set and list
#DICT METHODS
#create a empty dict
d= {}
#extend dict with another dict
d.update({1: 'c',2: 'd'})
print(d)
#extend dict with another list
#d.update([1,2,3])   type error, cannot convert
#extend dict with another tuple
#d.update(1,2,3)   type error
#extend dict with another set
#d.update({1,2,3})

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d={1:'a', 2:'b', 3:'c', 4:'d'}
#remove the pair with key 4
d.pop(4)   # remove the 4
print(d)
#remove the pair with key 100
#d.pop(100)  error, there is no pairs
#remove the pair with key 100 if not there return 'z'
print(d.get(100, 'z'))

#remove the last pair
d.popitem()
print(d)
#remove all elements from the dict
print(d.clear())    # None, if the values are empty

#create a dict with {1:'a', 2:'b', 3:'c', 4:'d'}
d={1:'a', 2:'b', 3:'c', 4:'d'}
#get the value of key 4
print(d.get(4))
#get the value of key 100
print(d.get(100))
#get the value of key 100, if key is not present get 'z'
print(d.get(100, 'z'))

#get the value of key 4 with setdefault
print(d.setdefault(4))   #d
#get the value of key 100 with setdefault
print(d.setdefault(100))   # None
print(d)
#get the value of key 100 with setdefault, if key is not there add 101 with 'z'
print(d.setdefault(101, 'z'))  # 100: None
print(d)
#get all keys of dict and print its type
print(d.keys())   # [1,2,3,4,100,101]
#get all values in dict and print its type
print(d.values())
#get all items in dict and print its type
print(d.items())

