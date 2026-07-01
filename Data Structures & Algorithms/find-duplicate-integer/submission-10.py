class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0],nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        newslow = 0
        while newslow != fast:
            newslow = nums[newslow]
            fast = nums[fast]
        return fast


        