import sys
#from math import sqrt, ceil

def getperiod(m) :
    prev = 0
    curr = 1
    count = 0

    while True :
        prev, curr = curr, prev + curr
        count += 1
        if prev % m == 0 and curr % m == 1 :
            return count

def get_fibonacci_huge_fast(n, m):
    count = getperiod(m)
    #print(count)
    f = n % count
    #print (f)
    if f <= 1 :
        return f
    prev, curr = 0, 1
    for i in range(2, f+1) :
        prev, curr = curr % m, (prev + curr) % m
    return curr % m

if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
