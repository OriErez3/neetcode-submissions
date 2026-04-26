class Solution:
    def solve(self, board: List[List[str]]) -> None:
        edges = []
        directions = ([0,1],[1,0],[-1,0],[0,-1])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1):
                    edges.append([r,c]) 
        def dfs(node):
            board[node[0]][node[1]] = "#"
            for dr,dc in directions:
                if node[0]+dr<len(board) and node[1]+dc<len(board[0]) and node[0]+dr>=0 and node[1]+dc>=0 and board[node[0]+dr][node[1]+dc] == "O":
                    dfs([node[0]+dr,node[1]+dc])
            return

        for i,j in edges:
            dfs([i,j])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
        for r in range(len(board)):
            for c in range(len(board[0])):    
                if board[r][c] == "#":
                    board[r][c] = "O"
        



        