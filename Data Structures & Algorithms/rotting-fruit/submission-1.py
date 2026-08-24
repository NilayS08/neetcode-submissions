class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,0), (-1,0) ,(0,1), (0,-1)]
        minute, freshOranges = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshOranges += 1
        while queue and freshOranges > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append((row,col))
                    freshOranges -= 1
            minute += 1
        return minute if freshOranges == 0 else -1