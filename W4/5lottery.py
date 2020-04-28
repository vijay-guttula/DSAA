import sys


def fast(p, b, e):
    count = 0
    i = 0
    while i < len(b):
        if p < b[i] or p > e[i]:
            return count
        if p >= b[i] and p <= e[i]:
            count += 1
            i += 1
    return count


def lot_naive(s, p):
    count_list = []
    for j in p:
        count = 0
        for i in s:
            if j >= i[0] and j <= i[1]:
                count += 1
        count_list.append(count)
    return count_list


if __name__ == '__main__':
    input = sys.stdin.readline()
    n = list(map(int, input.split()))
    s = []
    b = []
    e = []
    for i in range(n[0]):
        input = sys.stdin.readline()
        n1 = list(map(int, input.split()))
        # s.append(n1)
        b.append(n1[0])
        e.append(n1[1])
    b.sort()
    # print(b)
    e.sort()
    # print(e)
    # print(s[0][1])
    input = sys.stdin.readline()
    n1 = list(map(int, input.split()))
    # print(lot_naive(s, n1))
    for i in n1:
        # print(i)
        print(fast(i, b, e), end=" ")
