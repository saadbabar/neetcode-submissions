class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            sum_piles = 0
            for pile in piles:
                sum_piles += math.ceil(pile/mid)

            if sum_piles <= h:
                right = mid
            
            else:
                left = mid + 1
        return left