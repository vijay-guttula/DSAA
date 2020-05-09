def ED(m, n):
    dp = [[i for i in range(len(m) + 1)] for j in range(len(n) + 1)]
    # print(dp)
    for j in range(len(n) + 1):
        dp[j][0] = j
    # print(dp)

    for y in range(1, len(m) + 1):
        for x in range(1, len(n) + 1):
            insert_op = dp[x - 1][y] + 1
            delete_op = dp[x][y - 1] + 1
            match_op = dp[x-1][y-1]
            mismatch_op = dp[x-1][y-1] + 1

            if m[y-1] == n[x-1]:
                dp[x][y] = min(insert_op, delete_op, match_op)
            else:
                dp[x][y] = min(insert_op, delete_op, mismatch_op)

    return dp[len(n)][len(m)]


if __name__ == '__main__':
    distance = ED(input(), input())
    print(distance)
