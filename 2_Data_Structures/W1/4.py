if __name__ == '__main__':
    t = int(input())
    stack = []
    l = 0
    for i in range(t):
        x = input().split()
        if len(x) > 1:
            stack.append(int(x[1]))
            l += 1
        else:
            if x[0] == 'max':
                print(max(stack))
            else:
                del stack[len(stack) - 1]
