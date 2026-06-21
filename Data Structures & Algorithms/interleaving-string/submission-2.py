class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        if len(s1)+len(s2) != len(s3):
            return False
        def recursion(i,j):
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            k = i+j
            res = False
            if i < len(s1) and s1[i] == s3[k] and recursion(i+1,j):
                res = True
            if j < len(s2) and s2[j] == s3[k] and recursion(i,j+1):
                res = True
            dp[(i,j)] = res
            return res
        return recursion(0,0)