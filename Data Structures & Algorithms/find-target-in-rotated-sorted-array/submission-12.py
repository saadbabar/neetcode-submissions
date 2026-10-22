class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = None
        left, right = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                pivot = l
                break

            else:
                m = (l + r) // 2

                if (nums[m] < nums[r]):
                    r = m
                else:
                    l = m + 1

        if pivot == 0:
            left, right = 0, len(nums) - 1
        elif target >= nums[0]:
            left, right = 0, pivot - 1
        else:
            left, right = pivot, len(nums) - 1
    
        while left <= right:
            m = (left + right) // 2

            if target == nums[m]:
                return m
            elif target < nums[m]:
                right = m - 1
            else:
                left = m + 1

        return -1

