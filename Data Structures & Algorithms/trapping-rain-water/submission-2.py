class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        m1 = 0 
        m2 = 0
        ret = 0
        for i in range(len(height)):
            m1 = max(height[i], m1)
            m2 = max(height[j], m2)
            prefix[i] = m1
            suffix[j] = m2
            if j != 0:
                j -= 1
        for i in range(len(height)):
            ret += min(prefix[i], suffix[i]) - height[i]
        return ret