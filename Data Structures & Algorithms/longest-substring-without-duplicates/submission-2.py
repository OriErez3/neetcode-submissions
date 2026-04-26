class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        check = set()
        ret = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
                
            check.add(s[r])
            ret = max(ret, r-l+1) 
        return ret