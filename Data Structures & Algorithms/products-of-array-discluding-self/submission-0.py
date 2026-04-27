class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [None] * n
        postfix = [None] * n
        output = [None] * n

        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        postfix[n-1] = nums[n-1]
        for i in range (n-2,-1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        for i in range (0, n):
            if i==0:
                output[i] = postfix[i+1]
            elif i == n-1:
                output[i] = prefix[i-1]
            else:
                output[i] = postfix[i+1] * prefix[i-1]
        return output