import sys

cache = [0]

''' for storing cache'''


def cache_():
    for i in range(1, 5):
        cache.append(min((abs(i - 1) + 1), (abs(i - 3) + 1), (abs(i - 4) + 1)))


def coins(m):
    cache_()
    for i in range(5, m + 1):
        x = i - 1
        y = i - 3
        z = i - 4
        cache.append(min(cache[x] + 1, cache[y] + 1, cache[z] + 1))
    l = len(cache)
    return cache[l - 1]


if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(coins(m))
