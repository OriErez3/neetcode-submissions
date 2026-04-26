class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = ([0,1],[1,0],[-1,0],[0,-1])
        queue=deque()
        fresh = set()
        count = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append([r,c])
                    
                elif grid[r][c] == 1:
                    fresh.add((r,c))
        if not queue and not fresh:
            return 0
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                n = queue.popleft()
                for j, l in directions:
                    if n[0]+j < len(grid) and n[1]+l < len(grid[0]) and n[0]+j>=0 and n[1]+l>=0 and grid[n[0]+j][n[1]+l] == 1 :
                        queue.append([n[0]+j,n[1]+l])
                        fresh.remove((n[0]+j,n[1]+l))
                        grid[n[0]+j][n[1]+l] = 2
            count += 1
        if fresh:
            return -1
        else:
            return count 
                    
                    

        