class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]

        if not cost:
            return 0
        
        if len(cost) <= 2:
            return min(memo[0], memo[1])
        
        for i in range(2, len(cost)):
            memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])

        return min(memo[len(memo) - 1], memo[len(memo) - 2])