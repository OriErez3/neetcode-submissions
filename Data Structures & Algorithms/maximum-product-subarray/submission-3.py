class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lar_max = lar_min = result = nums[0]
        for n in nums[1:]:
            new_max = max(n,n*lar_max,n*lar_min)
            new_min = min(n,n*lar_max,n*lar_min)
            lar_max,lar_min = new_max, new_min 
            result = max(result, lar_max)
        return result
