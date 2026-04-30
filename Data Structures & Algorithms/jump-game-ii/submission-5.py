class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        count = 0
        t = True
        while r < len(nums)-1:
            farthest = max(i + nums[i] for i in range(l, r+1))
            l = r + 1
            r = farthest
            count += 1
        return count