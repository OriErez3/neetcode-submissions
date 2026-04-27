class Solution:
    from collections import deque
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = ([0,1],[1,0],[-1,0],[0,-1])
        treasure = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    treasure.append([r,c])
        queue = deque()
        for i in treasure:
            queue.append(i)
        count = 0
        while queue:
            count += 1
            for i in range(len(queue)):
                t = queue.popleft()
                for rr, rc in directions:
                    if t[0]+rr>=0 and t[0]+rr<len(grid) and t[1]+rc>=0 and t[1]+rc<len(grid[0]) and grid[t[0]+rr][t[1]+rc] == 2147483647:
                        queue.append([t[0]+rr,t[1]+rc])
                        grid[t[0]+rr][t[1]+rc] = count
        

        