# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j, m = l, l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m += 1
            a[i], a[m] = a[m], a[i]
            j += 1
            a[j], a[m] = a[m], a[j]
        if a[i] == x:
            m += 1
            a[m], a[i] = a[i], a[m]
    a[l], a[j] = a[j], a[l]
    return j, m


def partition2(a, l, r):
    x = a[l]  # pivot
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]  # swapping
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    # use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
