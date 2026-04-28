class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1]*(n+1)
        cache[1] = 1
        if n >= 2:
            cache[2] = 2
        def ways(n):
            if cache[n] != -1:
                return cache[n]
            else:
                cache[n] = ways(n-1)+ways(n-2)
                return cache[n]
        return ways(n)