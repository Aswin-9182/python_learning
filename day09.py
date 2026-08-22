list = [4, 3, 2, 5, 6]
#print elements in list with for each loop
for i in list :
    print(i)        # 4 3 2 5 6
#print elements in list with index based for loop
for x in range(len(list)) :
    print(x)        # 4 3 2 5 6
#skip printing even numbers in list
for i in range(4) :
    if i%2==0:
        continue
    print(i)        # 3 5
print()
#skip printing odd numbers in list
for i in list :
    if i%2==1:
        continue
    print(i)        # 4 2 6
print()
#when number 2 comes stop printing 
for i in list : 
    if i==5:
        break
    print(i)        # 4 3 2
#when first odd number comes stop printing
print()
for i in list :
    if i==2:
        break
    print(i)        # 4 3
#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
for i in range(1,11):
    print(i)        # 1 2 3 4 5 6 7 8 9 10
print('All numbers printed')
print()
#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
for i in range(1,11,2):
    if i==2:
        continue
    print(i)        # 1 3 5 7 9
print('All nimbers printed')
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for i in range(10,1,-1):
    if i==4:
        break
    print(i)        # 10 9 8 7 6 5
print('All numbers printed')
    
