class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for a in range(amount+1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a],dp[a-c]+1)
        if dp[-1] != float("inf"):
            return dp[-1]
        return -1