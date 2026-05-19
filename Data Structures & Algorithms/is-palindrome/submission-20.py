class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        l,r = 0, len(t)-1
        while l <= r:
            while l < len(t) and not t[l].isalnum(): 
                l += 1
            while r >= 0 and not t[r].isalnum():
                r -= 1
            if l >= r:
                break
            if t[l] != t[r]:
                return False
            l += 1
            r -= 1
        return True