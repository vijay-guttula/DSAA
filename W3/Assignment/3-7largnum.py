import sys

def sal(l, p) :
    x = all(x < 10 for x in p)
    if x :
        p.sort(reverse=True)
        print(*p, sep="")
        return
    r = []
    while True :
        if len(p) == 1:
            r.append(p[0])
            print(*r, sep="")
            return
        maxx,minn = p.index(max(p)), p.index(min(p))
        temp = p[maxx]
        temp = temp // 10
        if p[minn] < 10 and (p[minn] > temp % 10 and p[minn] >= p[maxx] % 10) :
            r.append(p[minn])
            del p[minn]
        else :
            r.append(p[maxx])
            del p[maxx]
        #x = p[i] if all(p[i] 

        
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    input = sys.stdin.readline()
    p = list(map(int, input.split()))
    sal(n, p)

