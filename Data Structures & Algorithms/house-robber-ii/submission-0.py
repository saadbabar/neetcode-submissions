class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        memo = [-1] * (len(nums) - 1)
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            memo[i] = max(memo[i - 1], memo[i - 2] + nums[i])

        memo2 = [-1] * len(nums)
        memo2[1] = nums[1]
        memo2[2] = max(nums[1], nums[2])

        for i in range(3, len(nums)):
            memo2[i] = max(memo2[i - 1], memo2[i - 2] + nums[i])

        return max(memo[-1], memo2[-1])
        