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
    #count = getperiod(10)
    count = 60 #as it is the period lenght of 10
    f = n % count

    if f <= 1 :
        return f
     
    prev, curr = 0, 1
    
    for i in range(2, f+1) :
        prev, curr = curr, (prev + curr) % 10
    return curr % 10
    


def getlastdigofpartialsum(n, m):
    
    #S(n) to S(m) = F(m+2) - F(n+1) as S(m) = F(m+2) - 1, and we took f(n+1), as we need to include f(n)
     
    a = (get_huge_fib_fast(m+2) + 10 - 1) % 10
    b = (get_huge_fib_fast(n+1) + 10 - 1) % 10
    return (a - b) % 10
    #the +10 is for just in case of negative value 
    
    


if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    print(getlastdigofpartialsum(n, m))
    
