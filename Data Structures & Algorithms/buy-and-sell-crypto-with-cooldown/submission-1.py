class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, cooldown, free = float("-inf"),0,0
        for i in range(len(prices)):
            hold, cooldown, free = max(hold, free-prices[i]), hold+prices[i], max(free,cooldown)    
        return max(cooldown,free)