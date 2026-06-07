class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = nums[0]
        maxSum = nums[0]
        for i in nums[1:]:
            count = max(i,count+i) 
            maxSum = max(maxSum, count) 
        return maxSum