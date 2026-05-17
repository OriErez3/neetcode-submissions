class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {n: i for i,n in enumerate(nums)}
        for i,n in enumerate(nums):
            temp = target-n
            if temp in dic and i != dic[temp]:
                return [i,dic[temp]]