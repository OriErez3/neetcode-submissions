class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        combination = []

        def dfs(i, total):
            if total == target:
                ret.append(combination.copy())
                return
            if total > target or i >= len(nums):
                return 

            #Use number and use same one         
            combination.append(nums[i])
            dfs(i, total+nums[i])
        

            
            combination.pop()
            dfs(i+1, total)
        dfs(0, 0)
        return ret