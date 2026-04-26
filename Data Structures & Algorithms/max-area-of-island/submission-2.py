class Solution:
    from collections import deque
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count = 0
                    queue = deque()
                    queue.append([r,c])
                    grid[r][c] = 0
                    count += 1
                    while queue:
                        t = queue.popleft()
                        for lr, lc in directions:
                            new_r, new_c = t[0]+lr,t[1]+lc
                            if new_r >= 0 and new_c >= 0 and new_r < len(grid) and new_c < len(grid[0]) and grid[new_r][new_c] == 1:                                
                                queue.append([new_r, new_c])
                                count += 1
                                grid[new_r][new_c] = 0
                    m = max(count,m)
        return m
                            
                    

