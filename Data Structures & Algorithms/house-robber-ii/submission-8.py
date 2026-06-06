class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1,prev2 = 0,0
        for i in range(len(nums)-1):
            curr = max(prev1,prev2+nums[i])
            prev1,prev2 = curr, prev1
        l = prev1
        prev1,prev2 = 0,0
        for i in range(1,len(nums)):
            curr = max(prev1,prev2+nums[i])
            prev1,prev2 = curr, prev1
        t = prev1
        return max(l,t)