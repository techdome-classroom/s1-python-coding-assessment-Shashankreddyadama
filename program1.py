class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 'W':
                return
            grid[i][j] = 'W'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    count += 1
                    dfs(i, j)
        return count