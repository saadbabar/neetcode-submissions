class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        cur_c = 1
        max_c = 0
        i = 1

        for num in nums:
            if num - 1 not in my_set:
                while True:
                    if num + i in my_set:
                        cur_c += 1
                        i +=1
                    else:
                        max_c = max(cur_c, max_c)
                        cur_c = 1
                        i = 1
                        break
        return max_c