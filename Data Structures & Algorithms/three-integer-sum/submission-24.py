class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 0, len(nums)-1
        ret = []
        for j in range(len(nums)):
            if nums[j] == nums[j-1] and j>0:
                continue
            l,r = j+1, len(nums)-1
            target = nums[j]
            while l<r:
                left, right = nums[l], nums[r]
                threeSum = left+right+target
                if threeSum == 0:
                    ret.append([left,target,right])
                    l+= 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l +=1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif threeSum > 0: 
                    r -= 1
                elif threeSum < 0:
                    l += 1
                
        return ret

