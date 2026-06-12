from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            t = queue.popleft()
            if t[0]+1 < len(grid) and grid[t[0]+1][t[1]] == land:
                grid[t[0]+1][t[1]] = grid[t[0]][t[1]] + 1
                queue.append((t[0]+1,t[1]))
            if t[0]-1 >= 0 and grid[t[0]-1][t[1]] == land:
                grid[t[0]-1][t[1]] = grid[t[0]][t[1]] + 1
                queue.append((t[0]-1,t[1]))
            if t[1]+1 < len(grid[0]) and grid[t[0]][t[1]+1] == land:
                grid[t[0]][t[1]+1] = grid[t[0]][t[1]] + 1
                queue.append((t[0],t[1]+1))
            if t[1]-1 >= 0 and grid[t[0]][t[1]-1] == land:
                grid[t[0]][t[1]-1] = grid[t[0]][t[1]] + 1
                queue.append((t[0],t[1]-1))