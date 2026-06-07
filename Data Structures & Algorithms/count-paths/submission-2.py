class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for j in range(len(dp[0])):
            dp[0][j] = 1
        for r in range(1,len(dp)):
            for c in range(1, len(dp[0])):
                dp[r][c] = dp[r-1][c]+dp[r][c-1]
        return dp[m-1][n-1]
