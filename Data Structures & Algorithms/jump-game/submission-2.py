class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # iterate through this
        # keep track of at each index, max of where we can get
        if not nums or len(nums) == 1:
            return True

        dp = [-1] * len(nums)
        goal = len(nums) - 1

        for i in range(0, len(nums) - 1):
            dp[i] = max(nums[i] + i, dp[i])

        for i in range(len(nums) - 2, -1, -1):
            if dp[i] >= goal:
                goal = i

        return goal == 0

            
        

