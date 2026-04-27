class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(i, j):
            stack = [[i, j]]
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if -1 < nr < len(grid) and -1 < nc < len(grid[0]):
                        if (nr, nc) not in visited and grid[nr][nc] == "1":
                            visited.add((nr, nc))
                            stack.append([nr, nc])
        
        
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == "1":
                    visited.add((i,j))
                    dfs(i, j)
                    num_islands += 1
        return num_islands
