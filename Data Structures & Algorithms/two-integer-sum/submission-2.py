class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashset:
                return [hashset[difference], i]
            hashset[n] = i
        return