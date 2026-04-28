class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1]*(amount+1)
        def dfs(n):
            if n<0:
                return float("inf")
            if cache[n] != -1:
                return cache[n]
            if n == 0:
                return 0
            else:
                cache[n] = 1 + min(dfs(n-coin) for coin in coins)
                return cache[n]
        d = dfs(amount)
        if d == float("inf"):
            return -1
        else:
            return d

            
                    