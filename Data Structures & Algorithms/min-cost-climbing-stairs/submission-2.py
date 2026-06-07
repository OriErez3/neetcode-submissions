class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        next1, next2 = 0,0
        for i in range(2,len(cost)+1):
            curr = min(next1+cost[i-1], next2+cost[i-2])
            next1,next2 = curr, next1
        return next1
