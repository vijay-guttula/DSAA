import sys


def check(s):
    stack = []
    indexes = []
    for i in range(len(s)):
        if s[i] in ['[', '{', '(']:
            stack.append(s[i])
            indexes.append(i)

        else:
            # print(i)
            if s[i] not in[')', ']', '}']:
                continue
            elif len(stack) == 0:
                return i + 1
            elif (stack[len(stack) - 1] == '[' and s[i] != ']') or (stack[len(stack) - 1] == '(' and s[i] != ')') or (stack[len(stack) - 1] == '{' and s[i] != '}'):
                return i + 1
            else:
                del stack[len(stack) - 1]
                del indexes[len(indexes) - 1]
    if len(stack) == 0:
        return 'True'
    else:
        return indexes[(len(indexes) - 1)] + 1


if __name__ == '__main__':
    s = list(input())
    if len(s) == 1:
        print(len(s))
        exit()
    n = check(s)
    if n == 'True':
        print("Success")
    else:
        print(n)
