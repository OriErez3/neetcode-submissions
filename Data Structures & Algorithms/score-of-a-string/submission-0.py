class Solution:
    def scoreOfString(self, s: str) -> int:
        cur = 0
        for i in range(len(s)-1):
            f1 = ord(s[i])
            f2 = ord(s[i+1])
            cur += abs(f1-f2)
        return cur

