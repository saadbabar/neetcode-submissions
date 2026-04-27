class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        res = 1
        accumulate = x

        n_abs = abs(n)

        for i in range(n_abs):
            res = x * res
        if n < 0:
            return 1/res
        return res
