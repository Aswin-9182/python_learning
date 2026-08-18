#create a list with 3 elements
#INSERT OPERATIONS
#appending
#add 5 types of non-sequence elements to it with append

a=[1, 2, 3]
a.append(4)

a.append(5.2)
a.append(6+4j)
a.append(True)
a.append(None)
print(a)   # [1, 2, 3, 4, 5.2, (6+4j), True, None]
 #add 5 types of sequences to it with append
#extending
b=[1, 2, 3]
b.append([4,5,6,7,8])
b.append((1,2,3))
b.append({4,2,6})
b.append('aswin')
b.append({'a':1, 'b':2})
print(b)  
#add 5 types of non-sequence elements to it with extend
a=[1,2,3]
a.extend([4])
a.extend([5.2])
a.extend([6+4j])
a.extend([True])
a.extend([None])
print(a)
#add 5 types of sequence elements to it with extend
l=[1,2,3]
l.extend([4,5,6,7,8])
l.extend((1,2,3))
l.extend('aswin')
l.extend({2,4,7})
l.extend({'a': 1, 'b':2})
print(l) 
#inserting
#insert an element at index 1 and print
l=[1,3,5]
l.insert(1,2)
print(l)   # [1,2,3,5]
#insert an element at index -1 and print
l.insert(-1,2)
print(l)  # [1,2,3,2,5]
#insert an element at index 10000 and print
l.insert(10000,9)
print(l)   # there is no index in 10000 so we can print at the end of the list
#insert an element at index -10000 and print
l.insert(-10000,0)
print(l)    # there is no index in -10000 so we can print at th

#DELETE OPERATIONS
#create a list with 1,2,1,3,4,1
#pop element at index 3 and print element and list
c=[1,2,1,3,4,1]
c.pop(3)
print(c)   # [1,2,1,4,1]
#pop last element and print element and list
c.pop(-1)
print(c)    # [1,2,1,4]
#remove first 1 from list and print element and list
c.remove(1)
print(c)   # [ 2,1,4]
#clear all elements in the list
c.clear()
print(c)  # it can be print empty list
#UPDATE OPERATIONS
#create a list with 3,2,1,5,4 
#sort the list in ascending and print
a=[3,2,1,5,4]
a.sort()
print(a)  # [1,2,3,4,5]
#create a list with 3,2,1,5,4 
#sort the list in descending and print
a=[3,2,1,5,4]
a.sort(reverse=True)
print(a)  # [5,4,3,2,1]
#create a list with 3,2,1,5,4 
#reverse the list and print
a=[3,2,1,5,4]
a.reverse()
print(a)   # [5,4,1,2,3]

#READ OPERATIONS
#create a list with 1,2,1,3,1, 2
#find count of 1 and 2 in list
a=[1,2,1,3,1,2]
print(a.count(1))   # 3
print(a.count(2))   # 2
#find index of 1 from start
print(a.index(1))
#find index of 1 from 2nd index
print(a.index(1,2))   # 
#find index of 1 from 5th index
#print(a.index(1,5))  value error , 1 is not in list

#TUPLE
#create a tuple with 1,2,1,3,1, 2
t=(1,2,1,3,1,2)
#find count of 1 and 2 in tuple
print(t.count(1))
print(t.count(2))
#find index of 1 from start
print(t.index(1))
#find index of 1 from 2nd index
print(t.index(1,2))
#find index of 1 from 5th index
#print(t.index(1,5)) value error, not in tuple





