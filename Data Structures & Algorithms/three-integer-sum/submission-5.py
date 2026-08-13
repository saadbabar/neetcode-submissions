class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 returned indices

        nums.sort()

        # -4, -1, -1, 0, 1, 2
        res = set()
        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (nums[i] + nums[j] + nums[k] == 0):
                    res.add((nums[i], nums[j], nums[k]))
                    # infinite loop at this point if you don't come up with case
                    k-=1

                if (nums[i] + nums[j] + nums[k] > 0):
                    k -= 1

                if (nums[i] + nums[j] + nums[k] < 0):
                    j += 1

        return list(res)