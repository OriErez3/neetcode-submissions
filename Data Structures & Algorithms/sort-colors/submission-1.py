class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        i=0
        r = len(nums)-1
        while i <= r:
            if nums[i] == 0:
                t = nums[l]
                nums[l] = 0
                nums[i] = t
                l+=1
                i += 1  
            elif nums[i] == 2:
                t = nums[r]
                nums[r] = 2
                nums[i] = t
                r-=1
            else:
                i += 1
    #[]