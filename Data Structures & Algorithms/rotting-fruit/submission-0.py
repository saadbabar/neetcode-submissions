class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        time = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i, j])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:
            
            q_len = len(queue)
            for i in range(q_len):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr == len(grid) or nc < 0 or nc == len(grid[0]) or grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue
                    grid[nr][nc] = 2
                    fresh -=1
                    queue.append([nr, nc])
            time += 1

        return time if fresh == 0 else -1



