# Uses python3
import sys
import random


def partition3(a, l, r, count):
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


def partition2(a, l, r, count):
    x = a[l]  # pivot
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            if j != i:
                a[i], a[j] = a[j], a[i]
                count += 1  # swapping
    a[l], a[j] = a[j], a[l]
    count += 1
    return j, count


def randomized_quick_sort(a, l, r, count):
    if l >= r:
        return
    #k = random.randint(l, r)
    #a[l], a[k] = a[k], a[l]

    m, count = partition2(a, l, r, count)
    print(count)
    randomized_quick_sort(a, l, m - 1, count)
    randomized_quick_sort(a, m + 1, r, count)
    return


if __name__ == '__main__':
    n = int(input())

    input = sys.stdin.readline()
    a = list(map(int, input.split()))
    count = 0
    randomized_quick_sort(a, 0, len(a) - 1, count)
    print(count)
