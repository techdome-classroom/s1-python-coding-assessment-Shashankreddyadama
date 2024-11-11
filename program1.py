class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        # Helper function for Depth-First Search
        def dfs(r, c):
            # Base case: Out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current land cell as water (visited)
            grid[r][c] = 'W'
            # Explore the 4 directions (Up, Down, Left, Right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right
        
        # Step 1: Mark all border-connected land cells as water
        # Traverse the first and last rows
        for i in range(cols):
            if grid[0][i] == 'L':
                dfs(0, i)
            if grid[rows - 1][i] == 'L':
                dfs(rows - 1, i)
        
        # Traverse the first and last columns
        for i in range(rows):
            if grid[i][0] == 'L':
                dfs(i, 0)
            if grid[i][cols - 1] == 'L':
                dfs(i, cols - 1)
        
        # Step 2: Count the distinct islands in the inner grid
        island_count = 0
        for i in range(1, rows - 1):  # Exclude the border rows
            for j in range(1, cols - 1):  # Exclude the border columns
                if grid[i][j] == 'L':  # Found an unvisited land cell
                    dfs(i, j)  # Perform DFS to mark the whole island
                    island_count += 1  # Increment the island count
        
        return island_count
