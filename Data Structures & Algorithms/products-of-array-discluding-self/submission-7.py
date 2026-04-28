class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        ret = [0]*len(nums)
        running = 1
        for i in range(len(nums)):
            prefix[i] = running
            running = running*nums[i]
        running = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = running
            running = running*nums[i]
        for i in range(len(ret)):
            ret[i] = prefix[i]*suffix[i]
        return ret