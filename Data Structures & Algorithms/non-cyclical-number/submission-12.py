class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num):
            c = 0
            for i in str(num):
                c += int(i)*int(i)
            return c
        seen = set()
        while True:
            n = helper(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            
        return False