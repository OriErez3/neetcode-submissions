class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        h = {}
        most=0
        res = 0
        for i in s:
            if i not in h:
                h[i] = 1
            else:
                h[i] = h[i]+1
            if h:
                most = max(h.values())
            while (((right-left)+1) - most > k):
                h[s[left]] =  h[s[left]]-1
                left += 1
            res = max(right-left+1, res)
            right += 1
       
        return res
            



        