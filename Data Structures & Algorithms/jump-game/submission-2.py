class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for checker in range(len(nums)-2,-1,-1):
            if nums[checker]+checker >= goal:
                goal = checker
        return goal == 0