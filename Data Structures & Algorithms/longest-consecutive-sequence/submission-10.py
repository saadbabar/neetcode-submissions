class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we could sort O(nlogn)
        my_set = set(nums) # O(1) lookup
        counter = 1
        max_c = 1

        for num in nums:
            if num - 1 in my_set:
                continue
            while True:
                if num + counter in my_set:
                    counter +=1
                    max_c = max(counter, max_c)
                else:
                    counter = 1
                    break

        return max_c if nums else 0
                    


