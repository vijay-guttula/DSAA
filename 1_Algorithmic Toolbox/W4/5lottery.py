import sys

# points are sorted
# beg and end points are sorted
# not done yet


def quick():
    c = []

    while j < len(p):
        if p[j] >= b[i] and p[j] <= e[i]:
            count += 1
            i += 1
        elif p[j] <= b[i] and p[j] >= e[i]:
            c.append(count)
            j += 1


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
        s.append((n1[0], 'left'))
        s.append((n1[1], 'right'))
    # b.sort()
    # .sort()

    input = sys.stdin.readline()
    n1 = list(map(int, input.split()))
    for i in n1:
        s.append((i, 'point'))
