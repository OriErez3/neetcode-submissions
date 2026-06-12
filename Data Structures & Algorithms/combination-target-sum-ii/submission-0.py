class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        s = sorted(candidates)
        ret = []
        def backtracking(i,path,total):
            if total == target:
                ret.append(path[:])
                return
            if i == len(candidates) or total > target:
                return
            path.append(s[i])
            total += s[i]
            backtracking(i+1,path,total)
            path.pop()
            total -= s[i]
            j = i+1
            while j < len(candidates) and s[j] == s[i]:
                j += 1
            backtracking(j,path,total)
        backtracking(0,[],0)
        return ret
