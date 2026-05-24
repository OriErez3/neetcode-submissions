class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        ret = 0
        check = set()
        while r < len(s):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            check.add(s[r])
            ret = max(r-l+1, ret)
            r += 1
        return ret
            
            