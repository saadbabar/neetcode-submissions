class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        seen = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j):
            counter = 1
            stack = [[i,j]]
            seen.add((i, j))

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if -1 < nr < len(grid) and -1 < nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        counter += 1
                        stack.append((nr, nc))
            return counter

        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in seen:
                   max_area = max(max_area, dfs(i, j)) 

        return max_area