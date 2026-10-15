class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix)
        
        while l < r:
            m = (l + r) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m
            else:
                print(matrix[m])
                a, b = 0, len(matrix[m])
                while a < b:
                    n = (a + b) // 2
                    if matrix[m][n] == target:
                        return True
                    elif target < matrix[m][n]:
                        b = n
                    else:
                        a = n + 1
                return False

        return False