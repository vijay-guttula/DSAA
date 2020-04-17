import time
import math

"""
The following is, achieving fibonacci number in O(1) time complexity by using recurrence relations concept.
After all we know that, f(n) = f(n-2) + f(n-1) but using recursion  we get a time complexity of O(2^n) which takes decades
when finding 10000th number. 

"""


def naive_fib(n):
    if n <= 1:
        return n
    else:
        return naive_fib(n-2) + naive_fib(n-1)


def fib(n):

    a = (((1 + math.sqrt(5)) / 2) ** n) / math.sqrt(5)
    b = (((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5)
    c = (a - b)

    return int(c)


if __name__ == '__main__':
    n = int(input())

    tic = time.time()

    print("Fib of {}th number using recurrence relation derivation is {} ".format(n, fib(n)))

    tok = time.time()

    print("\n Time taken is {} s".format(tok-tic))

    tic = time.time()

    print("Fib of {}th number using naive algo is {} ".format(n, naive_fib(n)))

    tok = time.time()

    print("\n Time taken is {} s".format(tok-tic))
