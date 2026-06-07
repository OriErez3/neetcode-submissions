class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 0
        prev1 = 1
        count = 0 
        for i in range(1,len(s)+1):
            cur = 0
            if int(s[i-1])>0:
                cur += prev1
            if s[i-2:i] and int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                cur += prev2
            prev1,prev2 = cur,prev1
        return prev1

        