class Solution:
    def findMin(self, nums: List[int]) -> int:
        mid = len(nums)//2
        right = len(nums)-1
        left = 0
        while left<right:
            mid = (right+left)//2
            if nums[mid] > nums[right]:
                left = mid+1
                
            elif nums[mid] < nums[right]:
                right = mid   
        return nums[left]
        



        