import sys
#from math import sqrt, ceil

'''def getperiod(m) :
    prev = 0
    curr = 1
    count = 0

    while True :
        prev, curr = curr, prev + curr
        count += 1
        if prev % m == 0 and curr % m == 1 :
            return count
'''
#use the above code to find the length of the period

def getlastdig(n, m):
    #count = 60
    #print(count)
    f = n % 60
    #print (f)
    if f <= 1 :
        return f
    sum = 1  
    prev, curr = 0, 1
    for i in range(2, f+1) :
        prev, curr = curr % m, (prev + curr) % m
        sum += curr
    return sum % 10


if __name__ == '__main__':
    n = int(input())
    print(getlastdig(n, 10))
    
