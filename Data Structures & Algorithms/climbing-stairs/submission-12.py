class Solution:
    def climbStairs(self, n: int) -> int:
        prev0, prev1 = 1,1
        for i in range(2,n+1):
            prev0,prev1 = prev1,prev0+prev1
        return prev1