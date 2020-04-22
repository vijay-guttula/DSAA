import sys


'''
First implement - not upto the mark, time limit exceeded (9.97 / 5)

def search(curr, x):
    count = 0
    for i in x:
        if curr == i:
            count += 1
    return count


def Maj(x, curr, l, r):
    m = len(x) // 2
    count = search(curr, x[l: m])
    if count > m:
        return 1
    else:
        count += search(curr, x[m: r])

    if count > m:
        return 1
    else:
        return 0
'''


def quick(x):
    x.sort()
    l, r = 0, len(x) // 2
    while(r < len(x)):
        if x[l] == x[r]:
            return 1
        else:
            l += 1
            r += 1
    else:
        return 0


if __name__ == '__main__':
    n = int(input())

    x = sys.stdin.readline()
    x = list(map(int, x.split()))

    print(quick(x))

'''
For the first implement.

    prev_maj = 0
    for i in range(0, len(x)):
        curr = x[i]
        if prev_maj == curr:
            continue

        count = Maj(x, curr, i, len(x))
        if count == 1:
            print(count)
            break
        prev_maj = x[i]
    if count == 0:
        print(count)
'''
