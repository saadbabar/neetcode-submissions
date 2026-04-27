class Solution:
    def climbStairs(self, n: int) -> int:
        rob1, rob2 = 1, 1

        for i in range(n - 1):

            temp = rob1
            rob1 += rob2
            rob2 = temp
        return rob1

        