import sys

def ad(n, a, b) :
    i, sum = 0, 0
    if n == 1:
        return a[0] * b[0]
    else :
        while i < n :
            j, k = a.index(min(a)), b.index(min(b))
            sum += (min(a) * min(b))
            del a[j]
            del b[k]
            i += 1
        return sum

if __name__ == '__main__' :
    n = int(input())
    x = sys.stdin.readline()
    a = map(int, x.split())
    x = sys.stdin.readline()
    b = map(int, x.split())

    print(ad(n, list(a),list(b)))

            
