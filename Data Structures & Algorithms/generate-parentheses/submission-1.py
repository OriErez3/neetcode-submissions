class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def backtracking(path):
            if len(path) == 2*n:
                ret.append(path[:])
                return 
            
            #if path.count("(") < path.count(")")
            
            if path.count("(") < n:
                backtracking(path+"(")
            if path.count("(") > path.count(")"):
                backtracking(path+")")
        backtracking("")
        return ret
            
            