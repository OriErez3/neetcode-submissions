class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        ret = 0
        while r >= l:
            val = min(heights[l],heights[r])*(r-l)
            ret = max(ret,val)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ret