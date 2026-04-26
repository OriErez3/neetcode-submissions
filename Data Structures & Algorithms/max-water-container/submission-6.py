class Solution:
    def maxArea(self, heights: List[int]) -> int:
        idx = 0
        idxr = len(heights)-1
        left = heights[idx]
        right = heights[idxr]
        maxArea = 0
        while idx != idxr:
            maxArea = max(maxArea, min(left,right)*(idxr-idx))
            if (left < right):
                idx += 1
                left = heights[idx]
            elif (right < left):
                idxr -= 1
                right = heights[idxr]
            else:
                if (heights[idx+1] > heights[idxr-1]):
                    idx += 1
                    left = heights[idx]
                else:
                    idxr -= 1
                    right = heights[idxr]
        return maxArea

