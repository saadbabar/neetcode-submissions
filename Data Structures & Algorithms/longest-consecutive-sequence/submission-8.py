class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cur = 0
        max_c = 0
        my_set = set(nums)

        for num in nums:
            if num - 1 not in my_set:
                cur += 1
                while True:
                    if num + cur in my_set:
                        cur += 1
                    else:
                        max_c = max(max_c, cur)
                        break
                cur = 0
        return max_c