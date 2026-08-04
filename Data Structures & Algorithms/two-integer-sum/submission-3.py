class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # the two indices that add up to the target cant be the same index.
        # we're going to need to use a hashmap
        # one pass, and we'd check if the current value + any value inside the dictionary is equal to the target, if so return the index pair

        my_map = defaultdict(int)

        for i, n in enumerate(nums):
            complement = target - nums[i]
            if complement in my_map:
                return [my_map[complement], i]
            my_map[n] = i