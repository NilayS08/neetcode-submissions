class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiagonal = set()
        negDiagonal = set()
        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in cols or (r+c) in posDiagonal or (r-c) in negDiagonal:
                    continue
                
                cols.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res