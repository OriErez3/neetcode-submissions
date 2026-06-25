class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        retp = 1
        retn = 1
        pos = 1
        neg = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                pos += 1
                neg = 1
                retp = max(pos,retp)
            elif nums[i] < nums[i-1]:
                neg += 1
                pos = 1
                retn = max(neg,retn)
            else:
                pos = 1
                neg = 1
        return max(retp,retn)