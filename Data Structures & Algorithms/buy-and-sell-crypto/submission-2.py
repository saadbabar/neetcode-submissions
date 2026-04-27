class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        left, right = 0, 1
        max_p = 0
        while right != len(prices):
            if prices[right] < prices[left]:
                left = right
                right = right + 1
            else:
                max_p = max(max_p, prices[right] - prices[left])
                right = right + 1
        return max_p

