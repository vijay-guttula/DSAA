# Uses python3
def calc_fib(n):
    prev,curr = 0, 1
    
    if n <= 1 :
        return n
    #instead of storing the numbers let's just store the last digit for less time
    for i in range (2, n+1) :
        prev, curr = curr % 10, (prev + curr) % 10
    return curr

n = int(input())
print(calc_fib(n))
