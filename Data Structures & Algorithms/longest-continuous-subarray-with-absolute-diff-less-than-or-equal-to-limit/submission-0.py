class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ret = 0
        l = 0
        for r in range(len(nums)):
            while abs(max(nums[l:r+1])-min(nums[l:r+1])) > limit:
                l += 1
            ret = max(ret, r-l+1)        
        return ret
            