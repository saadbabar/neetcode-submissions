class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if num in nums if num - 1 in nums, res += 1
        # 

        nums_set = set(nums)
        if not nums:
            return 0

        result = 0
        for num in nums_set:
            cur = 0
            if num - 1 not in nums_set:
                # beginning of a set
                cur += 1
                y = 1
                while num + y in nums_set:
                    cur += 1
                    y += 1
                result = max(cur, result)
        return result