class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if (board[i][j].isdigit() and board[i][j] in row_set):
                    return False
                row_set.add(board[i][j])

                if (board[j][i].isdigit() and board[j][i] in col_set):
                    return False
                col_set.add(board[j][i])
            

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                threes = set()
                for x in range(3):
                    for y in range(3):
                        if (board[i + x][j + y].isdigit() and board[i + x][j + y] in threes):
                            return False
                        threes.add(board[i + x][j + y])

        return True
