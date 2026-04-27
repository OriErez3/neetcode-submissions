class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        m = 0
        check = set()
        for r in range(len(s)):
            if s[r] in check:
                while s[l] != s[r]:
                    check.remove(s[l])
                    l += 1
                l += 1
            check.add(s[r])
            m = max(m, r-l+1)
        return m