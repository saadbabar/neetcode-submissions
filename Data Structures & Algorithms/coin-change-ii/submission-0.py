class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        def numWay_toMake(index:int, amount:int) -> int:
            if index == len(coins):
                return 1 if amount == 0 else 0
            if memo[index][amount] != -1:
                return memo[index][amount]

            take = 0
            if (amount - coins[index] >= 0):
                take = numWay_toMake(index, amount - coins[index])
            skip = numWay_toMake(index + 1, amount)

            memo[index][amount] = take + skip
            return memo[index][amount]

        return numWay_toMake(0, amount)