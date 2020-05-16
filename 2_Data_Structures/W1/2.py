import sys

'''
Observation - the numbers not in the list are the leaf nodes.
but searching from only leaves too takes O(n ** 2)



def height(n, tree):
    count = None
    height = 0
    for i in range(n):
        if i not in tree:
            j = tree[i]
            count = 0
            while j != -1:
                count += 1
                j = tree[j]
            height = max(height, count)
    return height + 1

'''


def height():
    for i in range(n):


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    input = sys.stdin.readline()

    tree = list(map(int, input.split()))

    print(height(n, tree))
