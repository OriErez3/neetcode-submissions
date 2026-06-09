class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {x: set() for x in range(9)}
        columns = {x:set() for x in range(9)}
        box = {x:set() for x in range(9)}
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue 
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])
                if board[r][c] in columns[c]:
                    return False
                columns[c].add(board[r][c])
                b = (r//3)*3+(c//3)
                if board[r][c] in box[b]:
                    return False
                box[b].add(board[r][c])
        return True