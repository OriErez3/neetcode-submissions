class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {x: set() for x in range(9)}
        columns = {x:set() for x in range(9)}
        box = {x:set() for x in range(9)}
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue 
                if board[i][j] in rows[i]:
                    return False
                else: 
                    rows[i].add(board[i][j])
                if board[i][j] in columns[j]:
                    return False
                else:
                    columns[j].add(board[i][j])
                bx = (i // 3)*3 + (j//3)
                if board[i][j] in box[bx]:
                    return False
                else:
                    box[bx].add(board[i][j])
        return True