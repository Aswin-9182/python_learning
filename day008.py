#LINK: https://www.hackerrank.com/challenges/py-if-else/problem
n= 3
if n % 2 == 1 :
    print('Weird')
elif 2 <= n <= 5 :
    print('Not Weird')
elif 6 <= n <=20 :
    print('Weird')
elif n >= 20 :
    print('Not Weird')
    
#LINK: https://www.hackerrank.com/challenges/write-a-function/problem

    year=int(input)
    if year % 400 :
        return True
    elif year % 100 :
        return False
    elif year % 4 == 0:
        return True
    else :
        return False
    

#take n, if n from 1 to 7 print dayname else print invalid day number
#e.g. 1 - Sunday, 2 - Monday, 3 - Tuesday
n = int(input('Enter the day number'))
match n:
    case 1: 
        print('Monday')
    case 2: 
        print('Tuesday')
    case 3: 
        print('Wednsday')
    case 4: 
        print('Thursday')
    case 5: 
        print('Friday')
    case 6: 
        print('Saturday')
    case 7: 
        print('Sunday')