class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        for i in nums:
            if i-1 not in s:
                t = i
                temp = 1
                while t+1 in s:
                    temp = temp+1
                    t = t+1
                count = max(temp,count)
        return count 
            