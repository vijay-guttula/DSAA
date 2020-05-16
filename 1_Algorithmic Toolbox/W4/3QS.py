# Uses python3
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j, m = l, l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m += 1
            if m != i:
                a[m], a[i] = a[i], a[m]

            j += 1
            if j != m:
                a[m], a[j] = a[j], a[m]
        elif a[i] == x:
            m += 1
            if m != i:
                a[i], a[m] = a[m], a[i]

    a[l], a[j] = a[j], a[l]
    return j, m


'''
def partition2(a, l, r):
    x = a[l]  # pivot
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]  # swapping
    a[l], a[j] = a[j], a[l]
    return j
'''


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    n = int(input())

    input = sys.stdin.readline()
    a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, len(a) - 1)
    for i in a:
        print(i, end=' ')
