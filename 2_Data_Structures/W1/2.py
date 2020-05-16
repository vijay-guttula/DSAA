import sys


def height(n, tree):
    max = None
    for i in range(n):
        count = 0
        if tree[i] == -1:
            continue
        else:
            j = tree[i]
            while j != -1:
                count += 1
                j = tree[j]
            if max == None:
                max = count
            elif max < count:
                max = count
    return max + 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    input = sys.stdin.readline()

    tree = list(map(int, input.split()))

    print(height(n, tree))

