class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        back2,back1 = nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            back2, back1 = back1, max(back1,back2+nums[i])
        return back1