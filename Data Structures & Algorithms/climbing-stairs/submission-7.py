class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [None]*(n+1)
        def dfs(number):
            if number == 1:
                return 1 
            if number == 0:
                return 1
            if cache[number]:
                return cache[number]
            cache[number] = dfs(number-1)+dfs(number-2)
            return cache[number]
        return dfs(n)