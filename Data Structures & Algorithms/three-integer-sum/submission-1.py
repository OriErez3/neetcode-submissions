class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            v = -1*nums[i]
            j = i+1
            k = len(nums)-1
            test = True
            while j<k:
                if nums[j]+nums[k] < v:
                    j = j+1
                elif nums[j]+nums[k] > v:
                    k = k-1
                elif nums[j]+nums[k] == v:
                    ret.append([-1*v, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j = j + 1
                    while j < k and k+1 < len(nums) and nums[k] == nums[k+1]:
                        k = k - 1
        return ret

