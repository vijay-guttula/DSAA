import sys

def MoneyChange(v) :
    denominations = [1, 5, 10]
    change = 0
    while v is not 0 :
        i = denominations.index(max(denominations))
        change += v // max(denominations)
        v %= max(denominations)
        del denominations[i]

    return change

if __name__ == '__main__':
    v = int(sys.stdin.readline())
    print(MoneyChange(v))
