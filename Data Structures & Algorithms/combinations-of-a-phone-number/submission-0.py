class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"1": None, "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ret = []
        if not digits:
            return []
        def backtracking(index, path):
            if len(path) == len(digits):
                ret.append(path[:])
                return
            
            for letter in d[digits[index]]:
                backtracking(index+1,path+letter)
        backtracking(0,"")
        return ret

                
                
