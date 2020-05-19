import sys

def process(buff,n,a,p):
    i = 0
    prev_time = None
    next_time = None
    count = 0
    while i < n:
        if prev_time == None:
            next_time = a[i] + p[i]
            prev_time = next_time
            print(a[i])
            count = count + 1
            i = i + 1 
        elif a[i] >= next_time:
            count = 0
            print(a[i])
            prev_time = next_time
            next_time = next_time + p[i]
            count = count + 1
            i = i + 1
        elif a[i] < next_time:
            if count >= buff:
            #continue here

            elif count < buff:
                count = count + 1
                print(next_time)
                prev_time = next_time
                next_time = next_time + p[i]
                i = i + 1
            else:
                print(-1)
                i = i + 1
        

if __name__ == '__main__':
    buff, n = map(int, input().split())
    a = []
    p = []
    for i in range(n):
        string = list(map(int, input().split()))
        a.append(string[0])
        p.append(string[1])
    process(buff,n,a,p)