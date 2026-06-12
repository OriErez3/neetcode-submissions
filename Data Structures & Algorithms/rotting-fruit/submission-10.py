from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ret = 0
        while queue:
            amount_needed = len(queue)
            rotted = False
            for i in range(amount_needed):
                t = queue.popleft()
                r,c = t[0],t[1]
                for radd,cadd in directions:
                    if r+radd < len(grid) and c+cadd < len(grid[0]) and r+radd >= 0 and c+cadd >= 0 and grid[r+radd][c+cadd] == 1:
                        grid[r+radd][c+cadd] = 2
                        rotted = True
                        queue.append((r+radd,c+cadd))
            if rotted:
                ret += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return ret