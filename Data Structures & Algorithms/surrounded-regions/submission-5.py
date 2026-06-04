class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border_os = set()
        for i in range(len(board)):
            if board[i][0] == "O":
                border_os.add((i,0))
            if board[i][len(board[0])-1] == "O": 
                border_os.add((i,len(board[0])-1))
        for j in range(len(board[0])):
            if board[0][j] == "O":
                border_os.add((0,j))   
            if board[len(board)-1][j] == "O": 
                border_os.add((len(board)-1,j))
        
        def dfs(i,j):
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return 
            if board[i][j] != "O":
                return
            board[i][j] = "#"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for r,c in border_os:
            dfs(r,c)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"
            
