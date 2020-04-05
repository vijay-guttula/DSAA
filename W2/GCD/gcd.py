# Uses python3
import sys

def gcd_fast(a, b):
    prev, curr = a, b
    while curr is not 0 :
        prev, curr = curr, prev % curr


    return prev

if __name__ == "__main__":
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))
