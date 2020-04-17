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

def getlastdig(n):
    #count = 60 for mod 10
    #print(count)
    n = n % 60
    sum = 1
    #print (f)
    if n <= 1 :
        return n
    
    prev, curr = 0, 1
    for i in range(2, n+1) :
        prev, curr = curr % 10, (prev + curr) % 10
        sum += (curr ** 2) % 10
    return sum % 10


if __name__ == '__main__':
    n = int(input())
    print(getlastdig(n))
    
