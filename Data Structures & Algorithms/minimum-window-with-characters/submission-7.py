class Solution:
    def minWindow(self, s: str, t: str) -> str:
        og = Counter(t)
        check = {}
        ret = ""
        if len(t)>len(s):
            return ""
        l,r = 0,0
        for r in range(len(s)):
            check[s[r]] = 1+check.get(s[r],0)
            while all(check.get(k, 0) >= og[k] for k in og):
                if len(s[l:r]) < len(ret) or ret == "":
                    ret = s[l:r+1]
                check[s[l]] = check.get(s[l],1)-1
                if check[s[l]] == 0:
                    del check[s[l]]
                l += 1
        return ret
            
                


        
           
            

        