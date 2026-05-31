class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char = {}
        ret = 0
        max_val = 0
        for r in range(len(s)):
            char[s[r]] = 1+char.get(s[r],0)
            max_val = max(max_val,char[s[r]])
            replacements = r-l+1-max_val
            if replacements > k:
                char[s[l]] = char[s[l]] - 1
                l += 1
            ret = max(ret, r-l+1)
        return ret


        
