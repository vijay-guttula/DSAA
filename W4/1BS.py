import sys


def binarysearch_loop(a, x):
    l, r = 0, len(a)
    while (l < r):
        m = (l + r) // 2
        if x == a[m]:
            return m
        if x < a[m]:
            r = m
        if x > a[m]:
            l = m + 1
    else:
        return -1


if __name__ == '__main__':
    a = sys.stdin.readline()
    a = list(map(int, a.split()))
    data = a[1:]

    b = sys.stdin.readline()
    b = list(map(int, b.split()))
    keys = b[1:]

    for x in keys:
        print(binarysearch_loop(data, x), end=' ')
