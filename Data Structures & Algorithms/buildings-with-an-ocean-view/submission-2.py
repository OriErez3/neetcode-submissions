class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = [(heights[0],0)]
        for i in range(1,len(heights)):    
            while stack and heights[i] >= stack[-1][0]:
                stack.pop()
            stack.append((heights[i],i))
        ret = []
        for n,i in stack:
            ret.append(i)
        return ret
    