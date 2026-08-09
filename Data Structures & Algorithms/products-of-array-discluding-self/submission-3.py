class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first and last number index, multiply by one
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        output = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i - 1] * nums[i - 1]

        # 0, 3 -> 3, 0
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                postfix[i] = 1
            else:
                postfix[i] = postfix[i + 1] * nums[i + 1]

        # 1 1 2 8
        # 48<-24<-6<-1
        for i in range(len(nums)):
            output[i] = postfix[i] * prefix[i]

        return output
