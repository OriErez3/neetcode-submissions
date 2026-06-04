class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        pacific_ret, atlantic_ret = set(), set()
        visited = set()
        for i in range(len(heights)):
            pacific.add((i,0))
            atlantic.add((i,len(heights[0])-1))
        for j in range(len(heights[0])):
            pacific.add((0,j))
            atlantic.add((len(heights)-1,j))
        avisited = set()
        pvisited = set()
        def dfs(i,j, ocean,visit):
            if (i,j) in visit:
                return
            if i >= len(heights) or j > len(heights[0]) or i < 0 or j < 0:
                return
            visit.add((i,j)) 
            ocean.add((i, j))
            if i+1 < len(heights) and heights[i+1][j] >= heights[i][j]:
                ocean.add((i,j))
                dfs(i+1,j,ocean,visit)
            if i-1 >= 0 and heights[i-1][j] >= heights[i][j]:
                ocean.add((i,j))
                dfs(i-1,j,ocean,visit)
            if j+1 < len(heights[0]) and heights[i][j+1] >= heights[i][j]:
                ocean.add((i,j))
                dfs(i,j+1,ocean,visit)
            if j-1 >= 0 and heights[i][j-1] >= heights[i][j]:
                ocean.add((i,j))
                dfs(i,j-1,ocean,visit)
        pacific_ret = pacific.copy()
        atlantic_ret = atlantic.copy()
        for i in pacific:
            r,c = i[0],i[1]
            dfs(r,c,pacific_ret,pvisited)
        for i in atlantic:
            r,c = i[0],i[1]
            dfs(r,c,atlantic_ret,avisited)
        g = atlantic_ret.intersection(pacific_ret)
        ret = []
        for i in g:
            ret.append(i)
        return ret

        