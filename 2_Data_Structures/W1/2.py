import sys


def make_tree(t, n):
    a = [[None]] * n
    i = 0
    stack = list()
    while i < n:

        if t[i] == -1:
            a[i] = 0
            i += 1
        else:
            if a[t[i]] is not None:
                a[i] = 1 + a[t[i]]
                i += 1
            else:
                stack.append(i)
                i += 1
    else:
        while len(stack) != 0:
            x = stack.pop(0)
            if a[t[x]] is None:
                stack.append(x)
                continue
            a[x] = 1 + a[t[x]]
    return max(a) + 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    input = sys.stdin.readline()

    tree = list(map(int, input.split()))

    print(make_tree(tree, n))
