class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [1] * len(nums)

        # prefix: we want to calculate the product of
        # everything before index i

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        postfix[(len(nums) - 1)] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        for i in range (0, len(nums)):
            if i == 0:
                output[0] = postfix[i + 1]
            elif i == len(nums) - 1:
                output[len(nums) - 1] = prefix[len(nums) - 2]
            else:
                output[i] = prefix[i - 1] * postfix[i + 1]
        return output