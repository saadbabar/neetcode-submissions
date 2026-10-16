class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = None
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            hours_taken = 0

            for num in piles:
                hours_taken += math.ceil(num/m)
            
            if hours_taken <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k
