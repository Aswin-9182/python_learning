#conditions
#if conditions by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print('true')

a=10
b=20
if a<=b:
    print('true')

a=10
b=5
if a>=b:
    print('true')


a=10
b=5
if a>=b:
    print('true')

a=10
b=30
if a!=b:
    print('not match')


a=13
b=13
if a==b:
    print('match')

a='python'
if a!='java':
    print('match')

a=int(input('Enter a value'))
b=int(input('Enter b value'))
if a<b:
      print('less')

#if condition by using llogical operator
#and,or,not
a=3
b=6
if a<b and b>a :
    print('true')

a=4
b=8
if a<=b and b>=a :
    print('true')


a=5
b=7
if a!=b and a==b :
    print('true')

a=9
b=12
if a<b or b>a :
    print('true')

a=12
b=14
if a<=b or a>=b:
    print('true')

a=4
b=9
if a!=b or a==b:
    print('true')

a=10
b=20
if not a<b:
    print('less')

a=10
b=20
if not a>b:
    print('less')


a=10
b=20
if not a<b and b>a:
    print('less')


#if condition by using identify operators
a=7
if type(a) is int:
    print('It is int')

a=int(input())
if type(a) is not int:
    print('True')

a=float(input())
if type(a) is float:
    print('It is float')

#if condition by using membership operator
a=2,3,4,5,6,7,8,9,10
if 5 in a:
    print('True')

a=2,3,4,5,6,7,8,9,10
if 20 in a:
    print('True')

a=int(input('a value')
if 30 in a:
      print('true')# erroe

a=[2,3,4,5,6,7,8,9,10]
b=int(input('Entervalue'))
if b in a:
      print('true')

#if conditions by using comparision operators
a=6
b=12
if a<b:
    print('less')
else:
    print('true')

a=6
b=3
if a>b:
    print('less')
else:
    print('false')

a=6
b=12
if a<=b:
    print('less')
else:
    print('true')

a=6
b=3
if a>=b:
    print('less')
else:
    print('true')
a=10
b=20
if a==b:
    print('equal')
else:
    print('not equal')

#if conditions by using logical operators
a=3
b=6
if a<b and b>a :
    print('true')
else:
    print('false')

a=9
b=12
if a<b or b>a :
    print('true')
else:
    print('false')


#if-elif-else conditions by using comparision operator
a=3
b=6
if a<b:
    print('less')
elif b>a:
    print('greater')
else:
    print('true')


a=3
b=6
if a==b:
    print('same')
elif b<a:
    print('true')
else:
    print('greater')


#logical operator
a=int(input())
b=int(input())
if a==b and a<b:
    print('True')
elif a<b or a>b :
    print('same')
elif not a!=b:
    print('greater')

#membership
a=[2,3,4,5,6,7,8,9,10]
b=int(input())
if b in a:
    print('same')
elif b not in a:
    print('not same')


#multiple if conditions by using comparision
a=4
b=8
if a<b:
    print('less')
if b>a:
    print('greater')
if a!=b:
    print('Not equal')

#multiple if conditions by using logical operator
a=int(input())
b=int(input())
if a<b and a<=b:
    print('greater')
if a==b or a!=b:
    print('or')
if a is not b:
    print('not same')
#membership operator
a=[2,3,4,5,6]
b=int(input())
if b in a:
    print('same')
if b not in a:
    print('not same')


#nested-if conditions
a=5
b=10
if a<b:
    print('less')
    if b>a:
        print('greater')

a=12
b=15
if a==b:
    print('less')
    if b>a:
        print('greater')

a=5
b=10
if a<b:
    print('less')
    if b==a:
        print('greater')

a=30
b=40
if a>b:
    print('less')
    if b>a:
        print('greater')
    else:
        print('true')

a=6
b=12
if a>b:
    print('less')
    if b>a:
        print('greater')
else:
    print('true')


a=5
b=10
if a<b:
    print('less')
    if b>a:
        print('greater')
    elif a!=b:
        print('Not equal')
    else:
        print('false')


#task 1: voting
age=int(input())
if age>=18:
    print('eligible')
else:
    print('not eligible')

#task2: even or odd
num=int(input())
if num%2==0:
    print('even')
else:
    print('odd')

#leap year or not
a=int(input())
if a%4==0:
    print('leap year')
else:
    print('not leap year')

#guest code
name=input()
if name=='Aswin':
    print('welcome',name)
else:
    print('welcome guest')

name=input()
list=['aswin','ashok','uday','prakash']
if name in list:
    print('welcome',name)
else:
    print('welcome guest')


#ovels
a=input().upper()
list=['A','E','I','O','U']
if a in list :
    print('it is ovel')
else:
    print('it is consonent')
    
#bakery
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

#pizza
b=input()
if b=='BBQ pizza':
    print(800)
elif b=='crispy chicken pizza':
    print(600)
elif b=='panner pizza':
    print(400)
elif b=='corn pizza':
    print(300)
elif b=='french frice':
    print(200)
else:
    print('Not available')


age=int(input())
marks=int(input())
att=int(input())
if 18<=age:
    print('eligible for vote')
if 80<=marks:
    print('eligible for schlorship')
if 80<=att:
    print('allow to write exams')

#social media login
user=input()
password=int(input())
if user=='aswin':
    if password==9182:
        print('login successfully')
    else:
        print('fail')
else:
    print('invalid credentials')
'''
user=input()
password=int(input())
if user=='aswin' and password==9182:
    print('login successfully')
else:
    print('invalid credentials')









