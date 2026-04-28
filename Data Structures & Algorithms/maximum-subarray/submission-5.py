class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        count = float('-inf')
        for i in range(len(nums)):
            if curSum < 0:
                curSum = nums[i]
                count = max(curSum,count)
            else:
                curSum += nums[i]
                count = max(curSum,count)
        return count