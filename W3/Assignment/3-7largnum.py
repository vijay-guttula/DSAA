import sys

def isgreater(dig, maxdig) :
    ab = str(dig) + str(maxdig)
    ba = str(maxdig) + str(dig)
    #x = int(ab)
    #y = int(ba)
    return ab >= ba


def sal(l, p) :
    x = all(x < 10 for x in p)
    if x :
        p.sort(reverse=True)
        print(*p, sep="")
        return
    r = []
    while len(p) is not 0 :
        maxdig = -1
        for digit in p :
            if isgreater(digit, maxdig) :
                maxdig = digit
                i = p.index(digit)
        r.append(maxdig)
        del p[i]
    print(*r, sep="")
    return

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    input = sys.stdin.readline()
    p = list(map(int, input.split()))
    sal(n, p)

