class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        i = 0
        j,k = 0, len(nums)-1
        while i < len(nums)-1:
            j = i+1
            k = len(nums)-1
            if nums[i] == nums[i-1] and i != 0:
                i += 1
                continue
            target = nums[i]*-1
            while j < k:
                if nums[j]+nums[k] > target:
                    k -= 1
                elif nums[j]+nums[k] < target:
                    j += 1
                elif nums[j]+nums[k] == target:
                    ret.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            i += 1
        return ret
        

                