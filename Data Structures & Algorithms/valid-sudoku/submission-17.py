class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = [set() for _ in range(9)]
        vertical = [set() for _ in range(9)]
        square = [set() for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in horizontal[row]:
                    return False
                horizontal[row].add(board[row][col])
                if board[row][col] in vertical[col]:
                    return False
                vertical[col].add(board[row][col])
                idx = (row//3)*3+(col//3)
                if board[row][col] in square[idx]:
                    return False
                square[idx].add(board[row][col])
        return True