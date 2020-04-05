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
    #count = 60 for mod 10
    #print(count)
    f = m % 60
    sum = 0
    #print (f)
    if f <= 1 :
        return f
    if n <= 1 :
        sum = n
    
    prev, curr = 0, 1
    for i in range(2, f+1) :
        prev, curr = curr % 10, (prev + curr) % 10
        if i >= n :
            sum += curr
    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(getlastdig(n, m))
    
