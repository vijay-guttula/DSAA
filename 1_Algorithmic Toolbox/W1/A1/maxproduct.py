import sys


def maxfast(n):
    n.sort()
    l = len(n)
    max = n[l-1]
    while n[l-2] == max:
        del n[l-2]
        l = len(n)
    min = n[l-2]

    return min * max


if __name__ == '__main__':
    num = int(input())
    input = sys.stdin.readline()
    n = list(map(int, input.split()))

    print(maxfast(n))
