#int
a=5
print(type(a))
#float
b=2.35
print(type(b))
#complex
c=2+5j
print(type(c))
#boolean
d=True
print(type(d))
#NoneType
e=None
print(type(e))
#string
f="1,2,3"
print(type(f))
#Range
g= range(1,10,5)
print(type(g))
#List
h=[1,2,3]
print(type(h))
#tuple
i=(1,2,3)
print(type(i))
#Set
j={1,2,3}
print(type(j))
#Dict
k={"a":"b","c":"d"}
print(type(k))

#int to float
l=float(a)
print(type(l))
#float to int
m=int(b)
print(type(m))
#int to str
n=str(a)
print(type(n))
#list to tuple
p=tuple(h)
print(type(p))
#tuple to list
q=list(i)
print(type(q))
#list to set
r=set(h)
print(type(r))
#range to list
s=list(g)
print(type(s))