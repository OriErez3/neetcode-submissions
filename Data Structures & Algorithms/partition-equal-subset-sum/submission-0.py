class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = [False]*((sum(nums)//2)+1)
        if sum(nums) %2 == 1:
            return False
        
        dp[0] = True
        for i in nums:
            for s in range((sum(nums)//2),i-1,-1):
                dp[s] = dp[s] or dp[s-i]
        return dp[(sum(nums)//2)]
