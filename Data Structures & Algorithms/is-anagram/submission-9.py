class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = Counter(s)
        m = Counter(t)
        if l == m:
            return True
        else:
            return False