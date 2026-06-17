class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ret = []
        cols = set()
        pos_diag = set()
        neg_diag = set()
        path = [["."] * n for _ in range(n)]
        def backtracking(row):
            if row == n:
                ret.append(["".join(r) for r in path])
                return
            for col in range(n):
                if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                    continue
                cols.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)
                path[row][col] = "Q"
                backtracking(row+1)
                cols.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
                path[row][col] = "."
        backtracking(0)
        return ret
