import sys

def prize(n) :
    r = []
    if n <= 2 :
        print(1)
        print(n)
    else :
        i = 0
        while True:
            if n - (i + 1) >= i + 2 :
                r.append(i+1)
                n -= (i + 1)
                i += 1
            else :
                r.append(n)
                print(len(r))
                print(*r, sep=" ")
                return               

if __name__ == '__main__' :
    n = int(sys.stdin.readline())
    prize(n)
