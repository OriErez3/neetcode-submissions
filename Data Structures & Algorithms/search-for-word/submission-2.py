class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        s = set()
        def dfs(i,j,l):
            if l == len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or (i,j) in s or board[i][j] != word[l]:
                return False
            s.add((i,j))
            l += 1
            guess = (dfs(i+1,j,l) or dfs(i-1,j,l) or dfs(i,j+1,l) or dfs(i,j-1,l))
            s.remove((i,j))
            return guess
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False