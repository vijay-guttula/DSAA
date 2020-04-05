# Uses python3
import sys

def gcd_naive(a, b):
    prev, curr = a, b
    while curr is not 0 :
        prev, curr = curr, prev % curr

#because lcm is the product of 2 numbers / gcd
    return (a * b) // prev

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
