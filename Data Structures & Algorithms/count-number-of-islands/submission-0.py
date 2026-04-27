class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        num_islands = 0


        def bfs(i, j):
            queue = collections.deque()
            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
            queue.append((i, j))
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if ((nr < 0 or nr == len(grid)) or (nc < 0 or nc == len(grid[0])) or (grid[nr][nc] == '0') or ((nr, nc) in visited)):
                        continue
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    visited.add((i, j))
                    num_islands += 1
        return num_islands