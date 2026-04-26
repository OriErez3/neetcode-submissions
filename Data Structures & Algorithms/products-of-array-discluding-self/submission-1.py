class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        for i, v in enumerate(nums):
            prod = 1
            for j, k in enumerate(nums):
                if j == i:
                    None
                else:
                    prod = prod*k
            ret.append(prod)
        return(ret)