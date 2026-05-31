class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        count = 1
        for i in range(len(nums)):
            prefix[i] = count 
            count *= nums[i]
        count = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = count
            count *= nums[i]
        print(suffix)
        print(prefix)
        return [x * y for x, y in zip(prefix, suffix)]
