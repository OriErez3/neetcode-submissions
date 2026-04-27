class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        ret = []
        for i in range(len(sort)):
            if sort[i] == sort[i-1] and i>0:
                continue
            l = i+1
            r = len(sort)-1
            while l < r:
                if sort[l]+sort[r] == -sort[i]:
                    ret.append([sort[i],sort[l],sort[r]])
                    while l < r and sort[l] == sort[l+1]:
                        l += 1
                    while l < r and sort[r] == sort[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif sort[l]+sort[r] > -sort[i]:
                    r -= 1
                else:
                    l += 1
        return ret