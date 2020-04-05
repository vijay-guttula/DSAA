# Uses python3
def calc_fib(n):
    a = [0,1]
    
    if n <= 1 :
        return n

    for i in range (2, n+1) :
        a.append(a[i-2] + a[i-1])
    return a[n]

n = int(input())
print(calc_fib(n))
