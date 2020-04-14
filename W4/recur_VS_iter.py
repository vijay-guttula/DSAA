import time
import sys
import numpy as np


def linear(num, List):
    found = False
    tic = time.time()
    for i in List:
        if i == num:
            found = True
            break
    tok = time.time()
    print("Time Taken by iteration is {:.5f} ms".format((tok - tic) * 1000))
    return


def linear_recur(i, num, List):
    if i >= len(List):
        return False
    if List[i] == num:
        return True
    else:
        return linear_recur(i+1, num, List)


if __name__ == '__main__':
    # List = sys.stdin.readline()
    # List = list(map(int, List.split()))
    # num = int(input())
    List = list(np.random.randint(low=0, high=500, size=500))
    num = np.random.randint(0, 500)
    linear(num, List)

    tic = time.time()
    b = linear_recur(0, num, List)
    tok = time.time()

    print("\nTime taken by recursion {:.5f} ms".format((tok-tic) * 1000))
