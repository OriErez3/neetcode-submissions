class Solution:
    from collections import Counter
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = Counter(nums)
        for k, v in r.items():
            if v > 1:
                return True
        return False