import sys
import time


def binarysearch_recur(a, x, l, r):
    if l >= r:
        return -1
    else:
        m = (l + r) // 2
        if x == a[m]:
            return m
        if x < a[m]:
            r = m - 1
            return binarysearch_recur(a, x, l, r)
        if x > a[m]:
            l = m + 1
            return binarysearch_recur(a, x, l, r)


def binarysearch_loop(a, x):
    l, r = 0, len(a)
    while (l < r):
        m = (l + r) // 2
        if x == a[m]:
            return m
        if x < a[m]:
            r = m - 1
        if x > a[m]:
            l = m + 1
    else:
        return -1


if __name__ == '__main__':
    a = sys.stdin.readline()
    a = list(map(int, a.split()))
    a.sort()

    b = sys.stdin.readline()
    b = list(map(int, b.split()))

    tic = time.time()
    for x in b:
        print(binarysearch_recur(a, x, 0, len(a)), end=' ')
    tok = time.time()
    print("\nTime taken by recursion: {}".format(tok-tic))

    tic = time.time()
    for x in b:
        print(binarysearch_loop(a, x), end=' ')
    tok = time.time()
    print("\nTime taken by loop: {}".format(tok-tic))
