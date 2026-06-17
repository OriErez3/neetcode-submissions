class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if (target + total) % 2 != 0 or abs(target) > total:
            return 0
        subSetT = (target + total) // 2
        dp = [0]*(subSetT+1)
        dp[0] = 1
        for num in nums:
            for i in range(subSetT, num-1,-1):
                dp[i] += dp[i-num]
        return dp[subSetT]
