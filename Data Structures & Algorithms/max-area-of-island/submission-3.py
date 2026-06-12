class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        def dfs(r,c):
            if r == len(grid) or c == len(grid[0]) or r < 0 or c < 0 or (r,c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        m = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                m = max(m,dfs(i,j))
        return m 
            