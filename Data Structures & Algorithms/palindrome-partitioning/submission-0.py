class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        def isPalindrome(a):
            return a[::-1] == a
        def backtracking(start,path):    
            if start == len(s):
                ret.append(path[:]) 
                return
            for end in range(start,len(s)):
                if isPalindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    backtracking(end+1,path)
                    path.pop()
        backtracking(0,[])
        return ret        
