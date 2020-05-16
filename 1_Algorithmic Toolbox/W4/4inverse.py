# Uses python3
import sys


def sort(arr):
    l = len(arr)
    # print(arr)
    if l == 1:
        return arr, 0
    else:
        a = arr[: l // 2]
        b = arr[l // 2:]

        a, ai = sort(a)
        b, bi = sort(b)

        c = []
        i, j = 0, 0
        count = 0 + ai + bi

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1

            else:
                c.append(b[j])

                j += 1
                count += len(a) - i

        c += a[i:]
        c += b[j:]

        return c, count


if __name__ == '__main__':
    n = int(input())  # Don't mind this, mandatory input, courseera's structure
    input = sys.stdin.readline()
    arr = list(map(int, input.split()))
    print(sort(arr)[1])
