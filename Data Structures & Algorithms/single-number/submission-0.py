class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)

        for value, freq in count.items():
            if freq == 1:
                return value