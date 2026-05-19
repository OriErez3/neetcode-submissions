class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        count = 0 
        l = 1
        for i in n:
            if i-1 not in n:
                l = 1
                while i + 1 in n:
                    l += 1
                    i += 1
                count = max(count,l)
        return count 