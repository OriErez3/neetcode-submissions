class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    queue = deque()
                    queue.append([r,c])
                    grid[r][c] = "0"
                    while queue:
                        rev = queue.popleft()
                        tr, tc = rev[0], rev[1]
                        for dr, dc in directions:
                            new_r, new_c = tr+dr, tc+dc
                            if new_r >= 0 and new_c >= 0 and new_r < len(grid) and new_c < len(grid[0]) and grid[new_r][new_c] == "1":
                                queue.append([new_r,new_c])
                                grid[new_r][new_c] = "0"
                        
                        
                    count += 1
        return count


                    
                