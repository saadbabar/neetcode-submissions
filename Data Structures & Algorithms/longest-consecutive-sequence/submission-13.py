class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        counter = 1
        max_check = 1

        for num in nums:
            if num - 1 in my_set:
                continue
            while num + counter in my_set:
                counter += 1
                max_check = max(max_check, counter)
            counter = 1

        return max_check if nums else 0


