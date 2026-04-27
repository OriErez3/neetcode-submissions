class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            d[n] = i
        for i, number in enumerate(nums):
            l = target-number
            if l in d and i != d[l]:
                return [i, d[l]]