import sys


def optimal_weight(W, w):
    dp = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(1, n+1):
        for weight in range(1, W+1):
            dp[i][weight] = dp[i-1][weight]
            if w[i-1] <= weight:
                val = dp[i-1][weight - w[i-1]] + w[i-1]
                if val > dp[i][weight]:
                    dp[i][weight] = val

    # return dp
    return dp[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    result = optimal_weight(W, w)
    print(result)
