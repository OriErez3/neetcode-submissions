class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        ret = []
        def backtracking(i,path):
            if i == len(s):
                ret.append(path[:])
                return 
            path.append(s[i])
            backtracking(i+1,path)
            path.pop()
            j = i+1
            while j < len(s) and s[j] == s[i]:
                j += 1

            backtracking(j,path)
        backtracking(0,[])
        return ret
        
            