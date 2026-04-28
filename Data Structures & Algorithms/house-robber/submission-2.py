class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*(len(nums)+1)
        def dfs(n):
            if n >= len(nums):
                return 0 
            if cache[n] != -1:
                return cache[n]
            else:
                cache[n] = max(dfs(n+1),nums[n]+dfs(n+2))
                return cache[n]
        return max(dfs(0),dfs(1))