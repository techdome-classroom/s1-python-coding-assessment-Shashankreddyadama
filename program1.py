class Solution: 
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:  # Check for an empty grid
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            # Base case for DFS: Out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark current land cell as water (visited)
            grid[r][c] = 'W'
            # Explore all 4 directions (Up, Down, Left, Right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right
        
        # Step 1: Mark all border-connected land cells (connected to the border)
        for i in range(rows):
            # Check first and last column (border columns)
            if grid[i][0] == 'L':
                dfs(i, 0)
            if grid[i][cols - 1] == 'L':
                dfs(i, cols - 1)
        
        for j in range(cols):
            # Check first and last row (border rows)
            if grid[0][j] == 'L':
                dfs(0, j)
            if grid[rows - 1][j] == 'L':
                dfs(rows - 1, j)
        
        # Step 2: Count the number of distinct islands in the remaining inner grid
        island_count = 1
        for i in range(1, rows - 1):  # Exclude the border rows
            for j in range(1, cols - 1):  # Exclude the border columns
                if grid[i][j] == 'L':  # Found an unvisited land cell
                    dfs(i, j)  # Perform DFS to mark the whole island
                    island_count += 1  # Increment the island count
        
        return island_count
