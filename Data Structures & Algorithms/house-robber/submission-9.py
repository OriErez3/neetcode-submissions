class Solution:
    def rob(self, nums: List[int]) -> int:
        take = 0
        skip = 0
        for i in range(len(nums)):
            take,skip = skip+nums[i],max(take,skip)
        return max(take,skip)