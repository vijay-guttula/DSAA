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

def get_huge_fib_fast(n) :
    #count = getperiod(m)
    count = 60 #as it is the period lenght of 10
    f = n % count

    if f <= 1 :
        return f
    
    prev, curr = 0, 1
    
    for i in range(2, f+1) :
        prev, curr = curr % 10, (prev + curr) % 10
    return curr % 10
    


def getlastdigofsum(n):
    
    #S(n) = f(n+2) - 1
    return (get_huge_fib_fast(n+2) - 1) % 10 #the +10 is for just incase of negative value

    


if __name__ == '__main__':
    n = int(input())
    print(getlastdigofsum(n))
    
