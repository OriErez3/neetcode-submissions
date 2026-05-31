class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        seen = set()
        ret = 0 
        while r < len(s):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1
            seen.add(s[r])
            ret = max(ret, r-l+1)
            r += 1
        return ret

            