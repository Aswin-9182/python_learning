#loops
#for,while, range, break,continue,pass
#for()
a=[10,20,30,40,50,60]
#print(a)
for i in a:
    print(i)

for i in a:
    print(a)

for i in a:
    print(i,end=' ')
print()
a=[5,6,7,8,9,10]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=(5,6,7,8,9,10)
for i in a:
    print(i)
print(type(a))
print(type(i))

a={5,6,7,8,9,10}
for i in a:
    print(i)
print(type(a))
print(type(i))

a={'name':'aswin','city':'kmm','year':2026}
for i in a:
    print(i)
print(type(a))
print(type(i))
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))

for i in a.values():
    print(i)
    print(type(a))
    print(type(i))

for i in a.items():
    print(i)
    print(type(a))
    print(type(i))

a=[4.5,6.7,8.9]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=['python','java','dsa']
for i in a:
    print(i)
print(type(a))
print(type(i))

a=[3+4j,4+9j]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=[True,False]
for i in a:
    print(i)
print(type(a))
print(type(i))

a=[4,2.5,3+4j,'asw',True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))
    
a=['vij','hyd','vzg']
b=[]
for i in a:
    b.append(i.upper())
print(b)


#while loop()
a=10
while a>1:
    print(a)

a=10
while a>1:
    print(a)
    a=a-1

a=10
while a>=1:
    print(a)
    a=a-1

a=10
while a>1:
    a=a-1
    print(a)
a=10
while a>1:
    a=a-1
print(a)

a=15
while a>1:
    print(a)
    a+=1

a=15
while a>1:
    print(a)
    a-=1
a=5
while a<20:
    print(a)
    a+=1
#voting
while True:
    age=int(input())
    if age>=18:
        print('eligible')
    else:
        print('not eligible')

#bakery
while True:
    a=int(input())
    if a==1200:
        print('redvelvet cake')
    elif a==1000:
        print('choco Almond')
    elif a==800:
        print('choclate')
    elif a==600:
        print('butter')
    else:
        print('cake is not available')


#Attendence Tracker
students=int(input('enter the no.of students:'))
p=0
a=0
for i in range(1,students+1):
    c=input(f"student {i} p/a")
    if c=='p':
        p+=1
    elif c=='a':
        a+=1
print('attendence tracker')
print('total no.of students',students)
print('total presenties:',p)
print('total absenties:',a)
            

#range
for i in range(10):
    print(i,end=' ')

for i in range(5,15):
    print(i,end=' ')

for i in range(0,20,2):
    print(i,end=' ')
print()
for i in range(5,50,5):
    print(i,end=' ')
print()
for i in range(3,30,3):
    print(i,end=' ')
print()

#students marks
while True:
    marks=int(input('Enter marks:'))
    for i in range(91,102):
        if i==marks:
            print('Grade A')
    for i in range(81,92):
        if i==marks:
            print('Grade B')
    for i in range(71,81):
        if i==marks:
            print('Gradec')
    for i in range(51,71):
        if i==marks:
            print('Grade c')
    for i in range(51):
        if i==marks:
            print('Fail')
        

while True:
    marks=int(input('Enter the marks:'))
    if marks in range(91,101):
        print('Grade-A')
    elif marks in range(81,91):
        print('Grade-B')
    elif marks in range(71,81):
        print('Grade-C')
    elif marks in range(51,71):
        print('Grade-D')
    else:
        print('Fail')



#break()
a=10
while a>1:
    print(a)
    a-=1
    if a==6:
        break

a=20
while a>1:
    a-=1
    if a==6:
        break
    print(a)

for i in range(25):
    if i==18:
        break
    print(i)

a='python'
for i in a:
    if i=='h':
        break
    print(i)

#continue
a=30
while a>10:
    a-=1
    if a==20:
        continue
    print(a)

for i in range(15):
    if i==10:
        continue
    print(i)

a='python'
for i in a:
    if i=='y':
        continue
    print(i)

#pass
for i in range(10):
    if i==5:
        pass
    print(i)

a=20
while a>5:
    print(a)
    a-=1
    if a==10:
        pass














