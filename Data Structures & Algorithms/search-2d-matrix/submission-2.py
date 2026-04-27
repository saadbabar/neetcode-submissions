class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1 # give us last list

        while l <= r:
            m = (l + r) // 2

            if target in matrix[m]:
                return True
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                r = m - 1

        return False