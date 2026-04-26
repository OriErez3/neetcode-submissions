class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
      
            
        def dfs(r,c, ocean):
            if ((r,c) in ocean):
                return
            ocean.add((r,c))
            for lr, lc in directions:
                nr, nc = r+lr,c+lc
                if nr >= 0 and nc >= 0 and nr < len(heights) and nc < len(heights[0]) and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc, ocean)
        for i in range(len(heights)):
           dfs(i,0,pacific)
           dfs(i, len(heights[0])-1,atlantic)
        for i in range(len(heights[0])):
           dfs(0,i,pacific)
           dfs(len(heights)-1,i,atlantic)
        
        
        return [list(cell) for cell in pacific & atlantic]


            


                