class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        t = Counter(nums)
        for i in t:
            if t[i] > 1:
                return True
        return False