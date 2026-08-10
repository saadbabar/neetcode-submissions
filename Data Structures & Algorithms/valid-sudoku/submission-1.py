class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] in row_set:
                    return False
                row_set.add(board[i][j]) if not board[i][j] == "." else None
                if board[j][i] in col_set:
                    return False
                col_set.add(board[j][i]) if not board[j][i] == "." else None
            col_set.clear()
            row_set.clear()

        # 3x3
        square = set()
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] in square:
                            return False
                        square.add(board[x][y]) if not board[x][y] == "." else None
                square.clear()
        return True

