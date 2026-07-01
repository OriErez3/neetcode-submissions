class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = 0
        ret = 0
        mult = 1
        for r in range(len(nums)):
            mult *= nums[r]
            while mult >= k and l < len(nums):
                mult //= nums[l]
                l += 1
            ret += r-l+1
        return ret
            