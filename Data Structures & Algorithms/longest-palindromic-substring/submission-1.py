class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        best = ""
        for i in range(len(s)):
            odd = check(i,i)
            even = check(i,i+1)
            longer = odd if len(odd) > len(even) else even
            if len(longer) > len(best):
                best = longer
        return best