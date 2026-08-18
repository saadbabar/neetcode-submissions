class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max variable
        # two pointer, a and b, while a < b we wanna
        # keep going

        maximum = 0
        left, right = 0, len(heights) - 1

        while left < right:
            current = min(heights[left], heights[right]) * (right - left)
            maximum = max(current, maximum)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maximum