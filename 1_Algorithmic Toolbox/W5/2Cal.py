import sys

cache = [0, 0]


def cache_():
    for i in (2, 3):
        if i % 2 == 0 and i % 3 == 0:
            x = i // 2
            y = i // 3
            z = i - 1
            cache.append(min(cache[x] + 1, cache[y] + 1, cache[z] + 1))
        elif i % 2 == 0 and i % 3 != 0:
            x = i // 2
            #y = i // 3
            z = i - 1
            cache.append(min(cache[x] + 1, cache[z] + 1))
        elif i % 2 != 0 and i % 3 == 0:
            #x = i // 2
            y = i // 3
            z = i - 1
            cache.append(min(cache[y] + 1, cache[z] + 1))
        else:
            z = i - 1
            cache.append(cache[z])


def calculation(m):
    cache_()
    if m < 4:
        return cache[m]

    for i in range(4, m + 1):
        if i % 2 == 0 and i % 3 == 0:
            x = i // 2
            y = i // 3
            z = i - 1
            cache.append(min(cache[x] + 1, cache[y] + 1, cache[z] + 1))
        elif i % 2 == 0 and i % 3 != 0:
            x = i // 2
            #y = i // 3
            z = i - 1
            cache.append(min(cache[x] + 1, cache[z] + 1))
        elif i % 2 != 0 and i % 3 == 0:
            #x = i // 2
            y = i // 3
            z = i - 1
            cache.append(min(cache[y] + 1, cache[z] + 1))
        else:
            z = i - 1
            cache.append(cache[z] + 1)
    return cache[len(cache) - 1]


def seq(n):
    s = [n]
    while n > 1:
        if n % 2 == 0 and n % 3 == 0:
            x = n // 2
            y = n // 3
            z = n - 1
            if cache[x] <= cache[y] and cache[x] <= cache[z]:
                s.append(x)
                n = n // 2
            elif cache[y] <= cache[x] and cache[y] <= cache[z]:
                s.append(y)
                n = n // 3
            else:
                s.append(z)
                n = n - 1
        elif n % 2 == 0 and n % 3 != 0:
            x = n // 2
            y = n // 3
            z = n - 1
            if cache[x] <= cache[y] and cache[x] <= cache[z]:
                s.append(x)
                n = n // 2
            else:
                s.append(z)
                n = n - 1
        elif n % 2 != 0 and n % 3 == 0:
            x = n // 2
            y = n // 3
            z = n - 1
            if cache[y] <= cache[x] and cache[y] <= cache[z]:
                s.append(y)
                n = n // 3
            else:
                s.append(z)
                n = n - 1
        else:
            z = n - 1
            s.append(z)
            n = n - 1
    return list(reversed(s))


if __name__ == '__main__':
    m = int(input())
    print(calculation(m))
    s = seq(m)
    print(*s, sep=" ")
