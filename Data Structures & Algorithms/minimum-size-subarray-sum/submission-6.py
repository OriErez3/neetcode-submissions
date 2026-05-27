class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0 
        ret = float("inf")
        count = 0
        while r < len(nums):
            count += nums[r]
            while count >= target:
                if l > r:
                    break
                ret = min(ret, r-l+1)
                count -= nums[l]
                l += 1
               
            r += 1
            
        return ret if ret !=float("inf") else 0