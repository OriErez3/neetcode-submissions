class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        checker = [False]*len(nums)
        def backtrack(index, cur):
            if len(cur) == len(nums):
                ret.append(cur[:])
                return
            
            for i in range(len(nums)):
                if checker[i] == False:
                    checker[i] = True
                    cur.append(nums[i])
                    backtrack(i,cur)
                    cur.pop()
                    checker[i] = False
        backtrack(0,[])
        return ret
