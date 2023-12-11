def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[-1] * (n+1) for _ in range(m+1)]
    def helper(i, j):
        if dp[i][j] != -1:
            return dp[i][j]
        if i == 0:
            dp[i][j] = j
        elif j == 0:
            dp[i][j] = i
        elif s1[i-1] == s2[j-1]:
            dp[i][j] = helper(i-1, j-1)
        else:
            dp[i][j] = 1 + min(helper(i-1, j), helper(i, j-1), helper(i-1, j-1))
        return dp[i][j]
    return helper(m, n)
