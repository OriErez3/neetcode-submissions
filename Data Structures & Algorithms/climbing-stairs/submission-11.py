class Solution:
    def climbStairs(self, n: int) -> int:
        prev2,prev1 = 1,1
        for i in range(n-1):
            cur = prev2+prev1
            prev2,prev1 = prev1,cur
        return prev1
          
        