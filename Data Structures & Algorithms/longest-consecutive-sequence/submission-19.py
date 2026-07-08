class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        if not nums: return 0
        m = 0
        for i in s:
            if i-1 not in s:
                j = i
                temp = 0
                while j in s:
                    temp += 1
                    m = max(temp,m)
                    j+=1
        return m