class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        starter, ender = 0, len(numbers) - 1
        while starter < ender:
            if numbers[starter] + numbers[ender] == target:
                return [starter + 1, ender + 1]
            elif numbers[starter] + numbers[ender] < target:
                starter += 1
            else:
                ender -= 1